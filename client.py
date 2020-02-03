import grpc
import message_pb2, message_pb2_grpc


# Open a gRPC channel
channel = grpc.insecure_channel("localhost:50051")

# create a stub
stub = message_pb2_grpc.CalculateSumStub(channel=channel)

# Call server
x = 100.1
y = 200.2

request = message_pb2.Addends(addend1=x, addend2=y)
response = stub.my_sum(request)

print("Sum:", response.sum)


