import socket

p = 8080
FORMAT = 'utf-8'
h = "localhost"
ADDR = (h, p)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

j1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

j1.connect((h, p))

while True:
    print("teste")
    # msg = j1.recv(1024)
    # print(msg.decode())
    msg = input()
    j1.send (msg.encode())

j1.close()