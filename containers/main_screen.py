from game.game_object import GameObject
from containers.table import Table
from components.button import Button


class MainScreen(GameObject):
    def __init__(self, navigator, client):
        self.table = Table((400, 100), navigator, client)
        self.navigator = navigator
        self.client = client

        self.button = Button((75, 50), 50, 'Sair', self.on_back)

    def on_back(self):
        self.client.close()
        self.navigator.navigate('start_connection')

    def render(self, game):
        game.add_component(self.button)
        self.table.render(game)
