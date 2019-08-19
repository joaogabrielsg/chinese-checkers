import pygame
from external_components.pygame_textinput import TextInput as TextInputCustom
from external_components.gif import GIFImage
from game.game_object import GameObject


class Gif(GameObject):
    def __init__(self, position, gif_path):
        GameObject.__init__(self, position, pygame.Rect(position[0] - 10, position[1] - 10 / 2, 10 * 2, 10))
        self.position = position
        self.gif = GIFImage(gif_path)

    def on_click(self):
        pass

    def update(self, screen, events):
        pass

    def render(self, screen):
        self.gif.render(screen=screen, pos=self.position)





