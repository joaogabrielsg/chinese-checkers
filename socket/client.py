from socket import* 

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

class Client():
    def __init__(self):
        self.port = port
		self.ip   = ip

        self.socket = socket(AF_INET, SOCK_STREAM)

    def connect(self):
        self.socket.connect((HOST, PORT))

    def server(self):
        self.socket.bind((HOST, PORT))
        self.socket.listen()
        connection, address = self.socket.accept()

        if connection:
             print('Connected by', addr)
