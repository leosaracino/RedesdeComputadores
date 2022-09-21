import threading
import socket


def main():
    FORMAT = 'utf-8'
    HEADER = 64

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(("192.168.1.65", 53))
    except:
        print('\nN conectou!\n')
        return 

    username = input('Usuario> ')
    print('\nConectado')

    def send(msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        print(client.recv(2048).decode(FORMAT))
    send(input())
    x = client.recv(1024)
    print(x)

#     thread1 = threading.Thread(target=receiveMessages, args=[client])
#     thread2 = threading.Thread(target=sendMessages, args=[client, username])

#     thread1.start()
#     thread2.start()


# def receiveMessages(client):
#     while True:
#         try:
#             msg = client.recv(2048).decode('utf-8')
#             print(msg+'\n')
#         except:
#             print('\nn permaneceu conectado!\n')
#             print('Pressione <Enter> Para continuar...')
#             client.close()
#             break
            

# def sendMessages(client, username):
#     while True:
#         try:
#             msg = input('\n')
#             client.send(('<{username}> {msg}'.format(username=username,msg=msg)).encode('utf-8'))
#         except:
#             return


main()