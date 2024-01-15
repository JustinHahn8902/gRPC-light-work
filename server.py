from concurrent import futures
import time

import grpc
import message_p_pb2
import message_p_pb2_grpc

class MessageServicer(message_p_pb2_grpc.MessagingServicer):

    def SingleMessage(self, request, context):
        print('The client sent a message:')
        print(request)
        reply = message_p_pb2.ServerMessage()
        reply.message = f'How is it going {request.name}? I got your message.'
        return reply

    def ServerStream(self, request, context):
        return super().ServerStream(request, context)

    def ClientStream(self, request_iterator, context):
        return super().ClientStream(request_iterator, context)

    def TwoWayStream(self, request_iterator, context):
        return super().TwoWayStream(request_iterator, context)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_p_pb2_grpc.add_MessagingServicer_to_server(MessageServicer(), server)
    server.add_insecure_port('localhost:45086')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
