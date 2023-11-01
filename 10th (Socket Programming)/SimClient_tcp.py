import socket

# Create a TCP client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ("localhost", 9999)

# Connect to the server
client.connect(server_address)

# Prompt the user to enter a name
name = input("Enter your name: ")

# Send the name to the server
client.send(name.encode('utf-8'))

# Close the client socket
client.close()