import socket
import ssl

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"

def clientEnd():
    # context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

    # # Load the self-signed certificate into the client's trust store (NOT RECOMMENDED FOR PRODUCTION)
    # context.load_verify_locations(cafile="certificate.crt")

    # context.load_cert_chain('new.pem', 'private.key')  # Your client certificate and key

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # c_client = context.wrap_socket(client, server_hostname="localhost", do_handshake_on_connect=False,
                                        # suppress_ragged_eofs=True)
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
    