from socket import *
import pickle
import threading

IP = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


class Client:
    def __init__(self, on_receive):
        self.ip = None
        self.port = None

        self.on_receive = on_receive

        self.socket = socket(AF_INET, SOCK_STREAM)

    def __start_server(self):
        self.socket.bind((self.ip, self.port))
        self.socket.listen()
        print('Aguardando .......')
        connection, address = self.socket.accept()
        if connection:
            print('Conectado a:', address)
            self.socket = connection
            thread = threading.Thread(target=self.receive_thread)
            thread.start()

    def receive(self):
        object_received = self.socket.recv(4096)
        self.on_receive(pickle.loads(object_received))

    def receive_thread(self):
        while True:
            self.receive()

    def send(self, send_object):
        self.socket.send(pickle.dumps(send_object))

    def close(self):
        self.socket.close()

    def start_connection(self, ip=IP, port=PORT):
        self.ip = ip
        self.port = port
        try:
            self.socket.connect((self.ip, self.port))
            thread = threading.Thread(target=self.receive_thread)
            thread.start()
        except:
            self.close()
            self.socket = socket(AF_INET, SOCK_STREAM)
            self.__start_server()
