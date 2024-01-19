# `socket` module, provides the basic socket functionality.
# `sctp` module, provides support for the SCTP protocol.

import socket
from sctp import *

# create an SCTP socket
# socket.AF_INET` argument specifies that the socket will use the IPv4 address family.

client_sock = sctpsocket_tcp(socket.AF_INET)

# connects the client socket to the server. 
# the `('localhost', 1234)` argument specifies the IP address and port number of the server.

client_sock.connect(('localhost', 1234))
print("Connected to the server.")

# within the loop, the client prompts the user to enter a message using the input() function.
# if the user enters "exit", the loop is terminated using the break statement.


# the client encodes it using the encode() method to convert it to bytes
# and sends it to the server using the sendall() method of the client socket (client_sock).

while True:
    message = input("Enter a message: ")
    if message == "exit":
        break

    # Send the message to the server
    client_sock.sendall(message.encode())

# Close the connection
client_sock.close()



# use try except in the case of handeling BrokenPipeError.
# try:
#     while True:
#         message = input("Enter a message: ")
#         if message == "exit":
#             break

#         # Send the message to the server
#         client_sock.sendall(message.encode())

# #if a BrokenPipeError occurs, it send the massage below.
# except BrokenPipeError:
#     print("The connection was closed by the server.")
# finally:
#     # Close the connection whether an exception occurs or not.
#     client_sock.close()