import socket

def main():
    
    try:
    
        # Creating socket using socket.socket() function
        # AF_INET=> Address Family for IPv4, AF_INET6 is for IPv6
        # SOCK_STREAM=> is for TCP, SOCK_DGRAM => is for UDP
        sfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        print("Socket Created Successfully")
        print("Socket Number=", sfd.fileno()) #prints unique no. associated with the socket sfd
        
        # Server Address => Server listens to local machine on port 1668
        servaddr = ('localhost', 1668)
        sfd.bind(servaddr) #bind allows server to recieve incoming connection
        print("Binding Successful")
        
        sfd.listen(2) #Socket can queue only 2 incomming reqs
        print("Socket is in Listen mode")
        
        com_s, cliaddr = sfd.accept() #waits till connection req from client.
        # created another socket specifically for communication
        print("Connection Established")
        
        while True:
            str = com_s.recv(100).decode('utf-8') #convert recieved message from utf-8 to string.
            print(f"String Recieved: {str}")
            
            if str == "exit":
                break
            
            message = input("Enter something:\n") #send message
            com_s.send(message.encode('utf-8')) # send in utf-8 encoding.
            
        sfd.close()
        
    except Exception as e:
        print(f"Socket connection failed: {e}")
        

if __name__ == '__main__':
    main()
        
    
    
    
    
    