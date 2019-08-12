import json
from game.game_object import GameObject
from components.button import Button


class StartConnection(GameObject):
    def __init__(self, position):
        GameObject.__init__(self, position)
        self.position = position
        self.cells = []

    def on_connect(self):
        print('Clicou')

    def render(self, game):
        button = Button((self.position[0], self.position[1] + 100), 100, 'Connectar', self.on_connect)
        game.add_component(button)
