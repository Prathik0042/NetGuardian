import socket
import threading
from trial import checkHTTPOrS
from isBlack import isBlack

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)           # blocking line
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"[{addr}]: {msg}") 
            if isBlack(msg):
                conn.send(f'http://localhost:8000/blacklisted.html'.encode(FORMAT))
            elif msg == DISCONNECT_MESSAGE:
                connected = False
            elif not checkHTTPOrS(msg):
                conn.send(f"http://localhost:8000/noHttps.html".encode(FORMAT))
            else:
                conn.send(msg.encode(FORMAT))

    conn.close()
           

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()    # blocking line
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[Starting] server is starting...")
start()