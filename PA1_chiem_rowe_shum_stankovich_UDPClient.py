"""
NAMES: Larry Chiem, Ian Rowe, Raymond Shum, Nicholas Stankovich
DUE DATE: May 11, 2021
ASSIGNMENT: Team Programming Assignment #1
DESCRIPTION: This was written in Python 3. This is the provided code for the UDP client. This client sends a message
addressed to the server through clientSocket for "best-effort" delivery. The UDP server capitalizes this message
and sends it back to the client. The client displays the capitalized message in the terminal.
"""

from socket import *        # Used to create sockets.
serverName = "localhost"    # Sets name of server to hostname (DNS will provide IP of localhost)
serverPort = 12000          # Sends to arbitrary port number of 1200 (to avoid well known hosts)

# Creates client socket declaring IPv4 and UDP datagrams.
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Modified to work with Python 3
message = input("Input lowercase sentence: ")

# Converts message to bytes and sends packet through clientSocket (source address attached by OS)
clientSocket.sendto(message.encode(),(serverName, serverPort))

# Unpacks message and server address from response (automatically attached to response)
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Displays capitalized message (translated from bytes)
print(modifiedMessage.decode())
clientSocket.close()

