import socket

def main():
    try:
        # Create a UDP socket
        sfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        servaddr = ('localhost', 1668)
        sfd.bind(servaddr)
        
        print("SOCKET CREATED SUCCESSFULLY")
        
        while True:
            buff, cliaddr = sfd.recvfrom(100)
            print("DATA RECEIVED FROM", cliaddr, ":", buff.decode('utf-8'))
            
            if buff.decode('utf-8') == "exit":
                break
            
            # Get a message from the server to send to the client
            message = input("Enter a message to send to the client:\n")
            sfd.sendto(message.encode('utf-8'), cliaddr)
        
        sfd.close()
    
    except Exception as e:
        print("Socket connection failed:", e)

if __name__ == '__main__':
    main()
