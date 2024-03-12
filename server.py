import socket
import threading
from trial import checkHTTPOrS

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"


# Open the file in read mode
with open('blacklisted.txt', 'r') as file:
    # Create an empty list to store the lines of the file
    BLACKLIST = []

    # Read each line of the file and append it to the lines list
    for line in file:
        BLACKLIST.append(line.strip())

# Print the lines list
#print(BLACKLIST)









#BLACKLIST = ['https://www.facebook.com', 'https://www.instagram.com', 'https://instagram.com', 'https://facebook.com']

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
            # conn.send(f"Message received: {msg}".encode(FORMAT)   
            if msg in BLACKLIST:
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