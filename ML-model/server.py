import grpc
from concurrent import futures
import activityPredictor_pb2
import activityPredictor_pb2_grpc

from prediction.prediction import Prediction

class ActivityPredictorServicer(activityPredictor_pb2_grpc.ActivityPredictorServicer):
    def Add(self, request, context):
        #result = request.num1 + request.num2

        pred = Prediction().predict()

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