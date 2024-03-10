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
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    print('Sending length...', send_length)
    client.send(send_length)
    print('Sending info...', message)
    client.send(message)
    # print(client.recv(2048).decode(FORMAT))   # "Message received"
    serverMsg = client.recv(2048).decode(FORMAT)     # Validation message
    return serverMsg

if __name__ == '__main__':
    client = clientEnd()
    print(sendMsg(client, "https://www.facebook.com/"))
    print(sendMsg(client, "http://httpforever.com/"))
    