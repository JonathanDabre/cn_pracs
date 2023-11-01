import socket

# Create a UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the server to a specific address and port
server_address = ("localhost", 9999)
server.bind(server_address)

print("UDP server is waiting for incoming messages...")

while True:
    data, client_address = server.recvfrom(1024)
    received_name = data.decode('utf-8')
    print(f"Received name from {client_address}: {received_name}")