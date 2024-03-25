import socket

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"

def clientEnd():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def sendMsg(client, msg):
    message = msg.encode(FORMAT)
    print('Sending info...', message)
    client.send(message)
    serverMsg = client.recv(2048).decode(FORMAT)     # Validation message
    return serverMsg

if __name__ == '__main__':
    client = clientEnd()
    print(sendMsg(client, "https://www.facebook.com/"))
    print(sendMsg(client, "http://httpforever.com/"))
    