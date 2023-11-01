import socket

# Create a UDP client socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ("localhost", 9999)

# Prompt the user to enter a name
name = input("Enter your name: ")

# Send the name to the server
client.sendto(name.encode('utf-8'), server_address)

# Close the client socket
client.close()