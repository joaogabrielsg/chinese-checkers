import Pyro4
import threading

SERVER_NAME = "PYRONAME:server"
CLIENT_NAME = "PYRONAME:client"


@Pyro4.expose
class Client(object):
    def __init__(self, game):
        self.daemon = Pyro4.Daemon()
        self.game = game
        self.server_name = Pyro4.locateNS()

        self.client_type = ''
        self.status_text = ''
        self.status_type = 0

        self.enemy = None

    def register_on_server_name(self, register_name):
        uri = self.daemon.register(Client)
        self.server_name.register(register_name, uri)

        thread = threading.Thread(target=self.daemon.requestLoop)
        thread.start()

    def start_connection(self):
        try:
            ns = self.server_name.lookup(SERVER_NAME)
            self.register_on_server_name(CLIENT_NAME)
            self.enemy = Pyro4.Proxy(SERVER_NAME)
        except:
            self.register_on_server_name(SERVER_NAME)
            self.enemy = Pyro4.Proxy(CLIENT_NAME)

    def teste(self):
        print('teste')
