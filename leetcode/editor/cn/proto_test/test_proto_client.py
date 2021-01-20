import grpc
from leetcode.editor.cn.proto_test import test_pb2, test_pb2_grpc


def run():
    # 连接 rpc 服务器
    channel = grpc.insecure_channel('localhost:50051')
    # 调用 rpc 服务
    stub = test_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(test_pb2.HelloRequest(name='ping'))
    print("Greeter client received: " + response.message)
    response = stub.SayHelloAgain(test_pb2.HelloRequest(name='ping again'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
