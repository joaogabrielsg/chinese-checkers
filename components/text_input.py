import pygame
from external_components.pygame_textinput import TextInput as TextInputCustom
from game.game_object import GameObject


class TextInput(GameObject):
    def __init__(self, position, size, font_size=35):
        GameObject.__init__(self, position, pygame.Rect(position[0] - size, position[1] - size / 2, size * 2, size))
        self.textinput = TextInputCustom(text_color=(255, 255, 255), cursor_color=(255, 255, 255), font_size=font_size)
        self.position = position

        self.text = ''

    def on_click(self):
        pass

    def clear(self):
        self.textinput.clear_text()

    def get_text(self):
        return self.text

    def update(self, screen, events):
        self.textinput.update(events)
        self.text = self.textinput.get_text()

    def render(self, screen):
        screen.blit(self.textinput.get_surface(), self.position)





