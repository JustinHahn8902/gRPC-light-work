import time

import grpc
import message_p_pb2
import message_p_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:45086') as channel:
        stub = message_p_pb2_grpc.MessagingStub(channel)
        print('1. Send a message. Get a message.')
        print('2. Send a message. Get some messages.')
        print('3. Send some messages. Get a message.')
        print('4. Send some messages. Get some messages.')
        choice = input('Which rpc call would you like to make: ')

        match choice:
            case '1':
                message = message_p_pb2.ClientMessage(name = 'Justin', message = 'This is one message.')
                reply = stub.SingleMessage(message)
                print('Single Response Received:')
                print(reply)
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case _:
                print('That is not an option.')

if __name__ == '__main__':
    run()
