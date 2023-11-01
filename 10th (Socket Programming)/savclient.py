import socket

class MyClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 6666))

    def run(self):
        try:
            message = "Hello server "
            self.client_socket.send(message.encode('utf-8'))
            self.client_socket.close()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    client = MyClient()
    client.run()
