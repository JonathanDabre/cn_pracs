import socket

class MyServer:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 6666))
        self.server_socket.listen(5)

    def run(self):
        try:
            while True:
                client_socket, addr = self.server_socket.accept()
                print('Got connection from', addr)
                data = client_socket.recv(1024).decode('utf-8')
                print('Message: ' + data)
                client_socket.close()
        except Exception as e:
            print(e)
        finally:
            self.server_socket.close()

if __name__ == '__main__':
    server = MyServer()
    server.run()
