import socket
import threading
from trial import checkHTTPOrS
from isBlack import isBlack
import ssl

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"

# context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# context.verify_mode = ssl.CERT_NONE
# context.load_cert_chain('new.pem', 'private.key')
# context.load_verify_locations(cafile='certificate.crt')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    msg = conn.recv(HEADER).decode(FORMAT)           # blocking line
    # You can use MissingSchema in requests library.
    if msg:
        print(f"[{addr}]: {msg}") 
        if isBlack(msg):
            conn.send(f'http://localhost:8000/blacklisted.html'.encode(FORMAT))
        elif not checkHTTPOrS(msg):
            conn.send(f"http://localhost:8000/noHttps.html".encode(FORMAT))
        else:
            conn.send(msg.encode(FORMAT))

    conn.close()
           
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # s_server = context.wrap_socket(server, server_side=True, do_handshake_on_connect=False,
        #                                 suppress_ragged_eofs=True)
        conn, addr = server.accept()    # blocking line
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[Starting] server is starting...")
start()