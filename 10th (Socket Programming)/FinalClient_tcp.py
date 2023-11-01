#tcp
import socket

def main():
    try:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        servaddr = ('localhost', 1668)
        
        sock.connect(servaddr) #connect to this address
        print("Connection Successfull")
        
        while True:
            message = input("\nEnter Something:\n")
            sock.send(message.encode('utf-8'))
            
            str = sock.recv(100).decode('utf-8')
            print(f"\nString recieved from server: {str}")
            
            if str == "exit":
                break
            
                    
    except Exception as e:
        print(f"Socket Connection failed: {e}")
        
    sock.close()
    
if __name__ == "__main__":
    main()