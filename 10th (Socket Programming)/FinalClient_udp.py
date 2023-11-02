#udp client
import socket

def main():
    try:
        # Create a UDP socket
        sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        servaddr = ('localhost', 1668)
        
        while True:
            message = input("ENTER STRING:\n")
            sockfd.sendto(message.encode('utf-8'), servaddr)
            
            if message == "exit":
                break
            
            # Receive and display a message from the server
            buff, servaddr = sockfd.recvfrom(100)
            print("MESSAGE RECEIVED FROM SERVER:", buff.decode('utf-8'))
            
            
    
    except Exception as e:
        print("Socket connection failed:", e)
    
    sockfd.close()

if __name__ == '__main__':
    main()
