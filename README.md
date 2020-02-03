# Simple client-server model with gRPC communication

### Service: calculate the sum of 2 numbers

### Install required packages using conda
    conda create --name grpc-env --file requirements.txt
    conda activate grpc-env

### Steps:
1. Write the core function: the function calculating sum of 2 variables was written in "core.py"
2. Make a proto file to define the messages and services: in "messages.proto"
3. Use the proto file to generate gRPC classes from .proto file
Run the command:

    python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. message.proto

Two files will be generated:
-  "message_pb2.py": contains defined messages
-  "message_pb2_grpc.py": contains server and client classes
 
4. Create the server: in "server.py"
- Create a wrapper class to take request and generate response
- Create a gRPC server and add the service to that server

5. Create the client: in "client.py"
- Open a gRPC channel
- Create a stub
- Create a request message
- Use the stub to call the service

### Executing
- Run command: 
    python3 server.py 
- Open other terminal, run command: 
    python3 client.py 