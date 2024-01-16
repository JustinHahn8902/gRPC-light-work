from concurrent import futures
import time
import random

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
        print('The client sent a message:')
        print(request)

        for i in range(random.randint(2, 11)):
            reply = message_p_pb2.ServerMessage()
            reply.message = f'Hi {request.name}! I just found out I can send lots of messages! This is message #{i}.'
            yield reply
            time.sleep(2)

    def ClientStream(self, request_iterator, context):
        print('The client is about to send a bunch of messages:')
        counter = 0
        for request in request_iterator:
            counter += 1
            print(request)

        reply = message_p_pb2.ServerMessage()
        reply.message = (f'Hi {request.name}! You sure sent a lot of messages just now! You sent {counter} messages! '
                         f'Well done!')
        return reply

    def TwoWayStream(self, request_iterator, context):
        print('The client is about to send a bunch of messages:')
        counter = 0
        for request in request_iterator:
            counter += 1
            print(request)

        for i in range(random.randint(2, 11)):
            reply = message_p_pb2.ServerMessage()
            reply.message = f'Hi {request.name}! I just found out I can send lots of messages! This is message #{i}.'
            yield reply
            time.sleep(2)

def runServer():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_p_pb2_grpc.add_MessagingServicer_to_server(MessageServicer(), server)
    server.add_insecure_port('localhost:45086')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    runServer()
