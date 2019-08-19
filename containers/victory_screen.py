from game.game_object import GameObject
from components.button import Button
from components.text import Text
from components.gif import Gif


class VictoryScreen(GameObject):
    def __init__(self, position, navigator, client):
        GameObject.__init__(self, position)
        self.position = position
        self.cells = []
        self.navigator = navigator
        self.client = client

        self.gif = Gif((self.position[0] - 140, self.position[1] - 20), 'tenor.gif')
        self.button = Button((self.position[0], self.position[1] + 350), 75, 'Continuar', self.on_confirm)
        self.text = Text((self.position[0], self.position[1] - 100), 100, 'Parabéns, você venceu!')

    def on_confirm(self):
        self.navigator.navigate('start_connection')

    def render(self, game):
        game.add_component(self.text)
        game.add_component(self.button)
        game.add_component(self.gif)
