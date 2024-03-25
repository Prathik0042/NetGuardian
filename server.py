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
    
    msg = conn.recv(HEADER).decode(FORMAT)           
    # You can use MissingSchema in requests library.
    if msg:
        print(f"[{addr}]: {msg}") 
        if isBlack(msg):
            conn.send(f'http://localhost:80/localhost/blacklisted.html'.encode(FORMAT))
        elif not checkHTTPOrS(msg):
            conn.send(f"http://localhost:80/localhost/noHttps.html".encode(FORMAT))
        else:
            conn.send(msg.encode(FORMAT))

    conn.close()
           
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()   
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[Starting] server is starting...")
start()