import threading
import socket

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 7777)) # trocar localhost por ip do servidor
    except:
        return print('Não conectado ao servidor')


def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8') #(trocar) para receber informações tabuleiro att
        except:
            print('Não está conectado no servidor!')
            client.close()
            break

def sendMessages(client):
    while True:
        try:
            msg = input() #(trocar) para enviar as informações da jogada do jogador
            client.send(msg.encode)
        except:
            return