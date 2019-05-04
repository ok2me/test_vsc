# Sockets can be configured to act as a server and listen for incoming messages,
# or connect to other applications as a client.
# After both ends of a TCP/IP socket are connected
# communication is [ bi-directional=capable of transmitting data in both directions (send and receive)
# but not at the same time]
# socket_echo_server.py
import socket
import sys

# It starts by creating a TCP/IP socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# then bind() is used to associate
# the socket with the server address
# Bind the socket to the port
server_address = ("localhost", 10000)
print("starting up on {} port {}".format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
# The integer argument is the number of connections
#  the system should queue up in the background before rejecting new clients.
sock.listen(1)
# When communication with a client is finished,
# the connection needs to be cleaned up using close().
# This example uses a try:finally block to ensure that close() is always called,
# even in the event of an error.
while True:
    # Wait for a connection
    print("waiting for a connection")
    # accept() returns an open connection between the server and client,
    # along with the address of the client.
    # The connection is actually a different socket
    # on another port (assigned by the kernel).
    # Data is read from the connection with recv()
    # and transmitted with sendall().
    connection, client_address = sock.accept()
    try:
        print("connection from", client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print("received {!r}".format(data))
            if data:
                print("sending data back to the client")
                connection.sendall(data)
            else:
                print("no data from", client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
