import grpc
import numpy as np
from concurrent import futures
import activityPredictor_pb2
import activityPredictor_pb2_grpc
import os
from dotenv import load_dotenv

from prediction.prediction import Prediction

class ActivityPredictorServicer(activityPredictor_pb2_grpc.ActivityPredictorServicer):
    def Add(self, request, context):
        # TODO this should probabably not be called every single request
        load_dotenv()

        api_key = dict(context.invocation_metadata()).get('api-key')
        if api_key != os.getenv("API_KEY"):
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details('Invalid API key')
            return activityPredictor_pb2.AddResponse()

        data = np.frombuffer(request.data, dtype=np.float32).reshape(request.rows, request.columns)

        pred = Prediction().predict(data)

        return activityPredictor_pb2.AddResponse(
            result=activityPredictor_pb2.PredictionDto(
                activity=pred.activity,
                accuracy=pred.accuracy
            ))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    activityPredictor_pb2_grpc.add_ActivityPredictorServicer_to_server(ActivityPredictorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()