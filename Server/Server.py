import socket
from sctp import *

# create an SCTP socket
server_sock = sctpsocket_tcp(socket.AF_INET)

# bind the socket to a specific address and port
server_sock.bind(('localhost', 1234))

# listen for incoming connections
# the `1` argument specifies that the server can accept a maximum of one incoming connection at a time.

server_sock.listen(1)
print("Server is listening for incoming connections...")

# accept a connection
client_sock, client_addr = server_sock.accept()
print(f"Accepted connection from {client_addr}")

# start handling incoming messages
while True:
    data = client_sock.recv(1024)
    if not data:
        break
    print(f"Received message from {client_addr}: {data.decode()}")

# close the connection
client_sock.close()