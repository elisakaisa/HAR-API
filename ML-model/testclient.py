import grpc
import numpy as np
import activityPredictor_pb2
import activityPredictor_pb2_grpc

def run():
    data = create_random_array()
    dataBytes = data.tobytes()

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = activityPredictor_pb2_grpc.ActivityPredictorStub(channel)
        response = stub.Add(activityPredictor_pb2.AddRequest(data=dataBytes, rows=data.shape[0], columns=data.shape[1]))
    print(f"Result: {response.result}")

def create_random_array():
    return np.random.uniform(-1, 1, size=(300, 6)).astype(np.float32) 

if __name__ == '__main__':
    input("Press to test gRPC connection")
    run()