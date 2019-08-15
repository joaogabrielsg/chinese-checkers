from connection.client import Client


class GameData:
    def __init__(self):
        self.messages = []
        self.cells = []


class GameClient(Client):
    def __init__(self):
        game_data = GameData()
        Client.__init__(self, game_data)

    def send_message(self, message):
        self.game_data.messages.append(message)
        self.send()
