import time

import grpc
import message_p_pb2
import message_p_pb2_grpc


def runClient():
    with grpc.insecure_channel('localhost:45086') as channel:
        stub = message_p_pb2_grpc.MessagingStub(channel)
        print('1. Send a message. Get a message.')
        print('2. Send a message. Get some messages.')
        print('3. Send some messages. Get a message.')
        print('4. Send some messages. Get some messages.')
        choice = input('Which rpc call would you like to make: ')

        match choice:
            case '1':
                c_name = input('Input your name: ')
                mes = input('Input a message to send: ')
                message = message_p_pb2.ClientMessage(name=c_name, message=mes)
                reply = stub.SingleMessage(message)
                time.sleep(1)
                print()
                print('The server just responded:')
                print(reply)

            case '2':
                c_name = input('Input your name: ')
                mes = input('Input a message to send: ')
                message = message_p_pb2.ClientMessage(name=c_name, message=mes)
                replies = stub.ServerStream(message)
                print()
                time.sleep(1)
                print('The server is responding many times:')
                for reply in replies:
                    print(reply)

            case '3':
                reply = stub.ClientStream(send_multiple_messages())
                time.sleep(1)
                print()
                print('The server just responded:')
                print(reply)

            case '4':
                replies = stub.TwoWayStream(send_multiple_messages())
                time.sleep(1)
                first = True
                for reply in replies:
                    if first:
                        print()
                        print('The server is responding many times:')
                    first = False
                    print(reply)

            case _:
                print('That is not an option. Try running the client again.')

def send_multiple_messages():
    print('Time to send some messages!')
    c_name = input('Input your name: ')
    while True:
        mes = input('Input a message to send (or nothing to finish): ')
        if mes == '':
            break
        message = message_p_pb2.ClientMessage(name=c_name, message=mes)
        yield message

if __name__ == '__main__':
    runClient()
