"""
NAMES: Larry Chiem, Ian Rowe, Raymond Shum, Nicholas Stankovich
DUE DATE: May 11, 2021
ASSIGNMENT: Team Programming Assignment #1
DESCRIPTION: Written in Python 3. This is the provided code for the TCP server. It listens for connection requests
on port 1200. Upon accepting a request from TCP client, it creates a new socket for communication. It receives a
sentence from TCP client, capitalizes it and sends it back to the client. Only the client will display the returned
string.
"""

from socket import *

serverPort = 12000                              # Listens on arbitrary port (to avoid well known ports)
serverSocket = socket(AF_INET, SOCK_STREAM)     # Create server socket using IPv4 and TCP
serverSocket.bind(("", serverPort))             # Establishes serverSocket as "welcoming socket"
serverSocket.listen(1)                          # Listen for TCP connections from client

print("The server is ready to receive")

# Waits until message is received from client - Closes after sending.
while True:
    # Accepts connection from client. Creates connectionSocket, dedicated to client.
    connectionSocket, addr = serverSocket.accept()

    # Decodes received message from client (from bytes, utf-8)
    sentence = connectionSocket.recv(1024).decode()

    # Capitalizes all letters in decoded sentence.
    capitalizedSentence = sentence.upper()

    # Encodes modified sentence in bytes & utf-8 and sends to client.
    connectionSocket.send(capitalizedSentence.encode())

    # Closes connection to client but server socket remains open.
    connectionSocket.close()
