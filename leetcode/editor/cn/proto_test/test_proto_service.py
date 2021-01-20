import time
from concurrent import futures

import grpc

from leetcode.editor.cn.proto_test import test_pb2, test_pb2_grpc


class Greeter(test_pb2_grpc.GreeterServicer):
    # 实现 proto 文件中定义的 rpc 调用
    def SayHello(self, request, context):
        return test_pb2.HelloReply(message='hello {msg}'.format(msg="pong"))

    def SayHelloAgain(self, request, context):
        return test_pb2.HelloReply(message='hello {msg}'.format(msg="pong again"))


def serve():
    # 启动 rpc 服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)  # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
