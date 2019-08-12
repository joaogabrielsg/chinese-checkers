import json
from game.game_object import GameObject
from components.button import Button
from components.text_input import TextInput


class StartConnection(GameObject):
    def __init__(self, position):
        GameObject.__init__(self, position)
        self.position = position
        self.cells = []

        self.text_input = TextInput((self.position[0], self.position[1] - 100), 100)

    def on_connect(self):
        print('==========')
        print(self.text_input.get_text())

    def render(self, game):
        self.button = Button((self.position[0], self.position[1] + 100), 100, 'Connectar', self.on_connect)
        game.add_component(self.text_input)
        game.add_component(self.button)
