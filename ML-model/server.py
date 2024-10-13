import grpc
from concurrent import futures
import activityPredictor_pb2
import activityPredictor_pb2_grpc

class ActivityPredictorServicer(activityPredictor_pb2_grpc.ActivityPredictorServicer):
    def Add(self, request, context):
        result = request.num1 + request.num2
        return activityPredictor_pb2.AddResponse(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    activityPredictor_pb2_grpc.add_ActivityPredictorServicer_to_server(ActivityPredictorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()