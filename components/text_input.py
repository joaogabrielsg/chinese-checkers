import pygame
from external_components.pygame_textinput import TextInput as TextInputCustom
from game.game_object import GameObject


class TextInput(GameObject):
    def __init__(self, position, size):
        GameObject.__init__(self, position, pygame.Rect(position[0] - size, position[1] - size / 2, size * 2, size))
        self.textinput = TextInputCustom(text_color=(255, 255, 255), cursor_color=(255, 255, 255))
        self.position = position

    def on_click(self):
        pass

    def update(self, screen, events):
        print(events)
        self.textinput.update(events)

    def render(self, screen):
        screen.blit(self.textinput.get_surface(), self.position)





