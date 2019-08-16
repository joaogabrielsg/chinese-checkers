from game.game_object import GameObject
from components.button import Button
from components.text_input import TextInput
from components.text import Text


class Chat(GameObject):
    def __init__(self, position, navigator, client):
        GameObject.__init__(self, position)
        self.navigator = navigator
        self.client = client

        # self.text = Text((self.position[0] - 200, self.position[1] - 85), 100, 'Endereço:')
        self.button = Button((self.position[0] + 100, self.position[1] + 200), 50, 'Enviar', self.send_message)
        self.text_input = TextInput((self.position[0] - 100, self.position[1] + 200), 100)

    def send_message(self):
        pass

    def render(self, game):
        game.add_component(self.text_input)
        game.add_component(self.button)
