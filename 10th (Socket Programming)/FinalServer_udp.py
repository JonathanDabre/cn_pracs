import socket

def main():
    try:
        # Create a UDP socket
        # we are using SOCK_DGRAM for UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        servaddr = ('localhost', 1668)
        sock.bind(servaddr)
        
        print("SOCKET CREATED SUCCESSFULLY")
        
        while True:
            buff, cliaddr = sock.recvfrom(100) #recvfrom => recievefrom since connectionless(udp)
            str = buff.decode('utf-8')
            print(f"DATA RECEIVED FROM {cliaddr} : {str}")
            
            if buff.decode('utf-8') == "exit":
                break
            
            message = input("Enter a message to send to the client:\n")
            sock.sendto(message.encode('utf-8'), cliaddr) #using sendto() coz udp.
        
        sock.close()
    
    except Exception as e:
        print("Socket connection failed:", e)

if __name__ == '__main__':
    main()
