import pygame
from game.game_object import GameObject


class Text(GameObject):
    def __init__(self, position, size, title, text_color=(255, 255, 255)):
        GameObject.__init__(self, position, pygame.Rect(position[0] - size, position[1] - size / 2, size * 2, size))
        self.size = size
        self.text_color = text_color
        self.title = title

        font = pygame.font.SysFont('Comic Sans MS', 40)
        self.text = font.render(self.title, True, text_color)
        self.textRect = self.text.get_rect()
        self.textRect.center = self.position

    def update(self, screen, dt):
        pass

    def on_click(self):
        pass

    def render(self, screen):
        screen.blit(self.text, self.textRect)
