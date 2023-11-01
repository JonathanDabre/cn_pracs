import socket

# Create a TCP server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ("localhost", 9999)
server.bind(server_address)

# Listen for incoming connections (1 connection at a time)
server.listen(1)

print("TCP server is waiting for incoming connections...")

while True:
    # Accept a connection from a client
    client_socket, client_address = server.accept()

    print(f"Accepted connection from {client_address}")

    # Receive data from the client (name)
    received_name = client_socket.recv(1024).decode('utf-8')
    print(f"Received name: {received_name}")

    # Close the client socket
    client_socket.close()