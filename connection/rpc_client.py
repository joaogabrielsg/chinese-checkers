import Pyro4
import threading

SERVER_NAME = "PYRONAME:checkers.server"
CLIENT_NAME = "PYRONAME:checkers.client"


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Client(object):
    def __init__(self):
        self.daemon = Pyro4.Daemon()
        self.server_name = Pyro4.locateNS()

        self.client_type = ''
        self.status_text = ''
        self.status_type = 0

        self.enemy = None

    def register_on_server_name(self, register_name, client_object):
        uri = self.daemon.register(client_object)
        self.server_name.register(register_name, uri)

        thread = threading.Thread(target=self.daemon.requestLoop)
        thread.start()

    def start_game(self, client_object): #start_game
        try:
            ns = self.server_name.lookup("checkers.server")
            self.register_on_server_name("checkers.client", client_object)
            self.enemy = Pyro4.Proxy(SERVER_NAME)
            self.status_text = 'Conectado'
            self.status_type = 1
            self.client_type = 'client'
        except:
            self.register_on_server_name("checkers.server", client_object)
            self.enemy = Pyro4.Proxy(CLIENT_NAME)
            self.status_text = 'Conectado'
            self.status_type = 1
            self.client_type = 'server'
