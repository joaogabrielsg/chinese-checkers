from game.game_object import GameObject
from containers.table import Table
from containers.chat import Chat
from components.button import Button
from components.title import Title


class MainScreen(GameObject):
    def __init__(self, navigator, client):
        self.table = Table((400, 100), navigator, client)
        self.chat = Chat((1000, 200), navigator, client)
        self.navigator = navigator
        self.client = client

        self.button = Button((75, 50), 50, 'Sair', self.on_back)

    def on_back(self):
        self.client.close()
        self.navigator.navigate('start_connection')

    def render(self, game):
        game.add_component(self.button)
        game.add_component(Title((600, 40), 100, self.navigator, self.client))
        self.table.render(game)
        self.chat.render(game)
