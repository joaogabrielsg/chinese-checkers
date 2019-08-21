from game.game_object import GameObject
from components.button import Button
from components.text_input import TextInput
from components.text import Text
from components.gif import Gif


class InputIp(GameObject):
    def __init__(self, position, navigator, client):
        GameObject.__init__(self, position)
        self.position = position
        self.cells = []
        self.navigator = navigator
        self.client = client

        self.gif = Gif((self.position[0] - 280, self.position[1] - 200), 'address.gif')
        self.button = Button((self.position[0], self.position[1] + 320), 75, 'Connectar', self.on_connect)
        self.text = Text((self.position[0] - 200, self.position[1] + 212), 100, 'Endereço:')
        self.text_input = TextInput((self.position[0] - 50, self.position[1] + 200), 100)

    def on_connect(self):
        ip = self.text_input.get_text()

        self.navigator.navigate('input_port', ip)

    def render(self, game):
        game.add_component(self.text_input)
        game.add_component(self.text)
        game.add_component(self.button)
        game.add_component(self.gif)
