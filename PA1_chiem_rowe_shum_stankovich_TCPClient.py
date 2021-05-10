"""
NAMES: Larry Chiem, Ian Rowe, Raymond Shum, Nicholas Stankovich
DUE DATE: May 11, 2021
ASSIGNMENT: Team Programming Assignment #1
DESCRIPTION: Written in Python 3. This is the provided code for the TCP Client. It establishes a TCP connection with
the TCP server and sends input in the form of a user entered sentence. The TCP Server capitalizes all words in the
sentence and sends it back to the client.
"""

from socket import *        # Used to create sockets

serverName = "localhost"    # Sets servername to host device (DNS maps IP address)
serverPort = 12000          # Arbitrary port used to avoid well known ports

# Creates client socket, specifying IPv4 and TCP socket.
clientSocket = socket(AF_INET, SOCK_STREAM)

# Initiates and establishes TCP connection with TCP server.
clientSocket.connect((serverName, serverPort))

# Accepts user input - Modified to work with Python 3.
sentence = input("Input lowercase sentence: ")

# Sends through TCP socket: sentence encoded as bytes using utf-8 (default)
clientSocket.send(sentence.encode())

# Receives modified string from TCP server (buffer size 1024)
modifiedSentence = clientSocket.recv(1024)

# Prints decoded (converted from bytes) string from TCP server
print("From Server: ", modifiedSentence.decode())

# TCP client sends message to TCP server to close connection
clientSocket.close()
