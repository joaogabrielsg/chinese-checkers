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
        uri = self.daemon.register(self.game)
        self.server_name.register(register_name, uri)

    def start_connection(self):
        greeting_maker = Pyro4.Proxy(SERVER_NAME)
        print(greeting_maker)
        if greeting_maker:
            self.enemy = greeting_maker
            self.register_on_server_name(SERVER_NAME)
        else:
            self.enemy = Pyro4.Proxy(CLIENT_NAME)
            self.register_on_server_name(CLIENT_NAME)

        thread = threading.Thread(target=self.daemon.requestLoop)
        thread.start()
