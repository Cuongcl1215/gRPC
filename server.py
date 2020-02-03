import grpc
import message_pb2
import message_pb2_grpc
import time
from concurrent import futures

def my_sum(x,y):
    return x+y

# Create a wrapper class to generate response from input request
class SumServicer(message_pb2_grpc.CalculateSumServicer):
    def my_sum(self, request, context):
        response = message_pb2.Sum()
        # get the value of the response by calling the defined function
        response.sum = my_sum(request.addend1, request.addend2)
        return response

# Create a grpc server then add a servicer instance to that server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
message_pb2_grpc.add_CalculateSumServicer_to_server(servicer=SumServicer(), server=server)

server.add_insecure_port("localhost:50051")
print("Starting server, listening on port 50051...")
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
    print("Server stopped!")