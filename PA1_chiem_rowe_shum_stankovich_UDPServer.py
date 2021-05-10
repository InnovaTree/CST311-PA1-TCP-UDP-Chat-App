"""
NAMES: Larry Chiem, Ian Rowe, Raymond Shum, Nicholas Stankovich
DUE DATE: May 11, 2021
ASSIGNMENT: Team Programming Assignment #1
DESCRIPTION: This was written in Python 3. UDP server listens on port 1200 (arbitrary) for a message from the UDP
client. It capitalizes the message and sends it back to the client. Confirmation is provided on the client terminal
window.
"""


from socket import *                            # Used to create socket objects.
serverPort = 12000                              # Arbitrary port used for listening.
serverSocket = socket(AF_INET, SOCK_DGRAM)      # Creates socket with parameters: IPv4 and UDP datagram

serverSocket.bind(("", serverPort))             # Assigns port 1200 to server socket.
print("The server is ready to receive")

# Continuously listens for message from clients.
while True:
    # Unpacks message and client's IP address once received.
    message, clientAddress = serverSocket.recvfrom(2048)

    # Decodes message from bytes, capitalizes all letters and assigns result to modifiedMessage
    modifiedMessage = message.decode().upper()

    # Sends capitalized message (encoded into bytes) to client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
