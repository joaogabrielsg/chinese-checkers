import pygame
from game.game_object import GameObject


class Background(GameObject):
    def __init__(self, color, position, height, width):
        GameObject.__init__(self, position, pygame.Rect(position[0] - width / 2, position[1] - height / 2, height, width))
        self.color = color
        self.vertices = [(position[0] - (width / 2), position[1] - (height / 2)),
                         (position[0] - (width / 2), position[1] + (height / 2)),
                         (position[0] + (width / 2), position[1] + (height / 2)),
                         (position[0] + (width / 2), position[1] - (height / 2))]

    def update(self, screen, dt):
        pass

    def on_click(self):
        pass

    def render(self, screen):
        pygame.draw.polygon(screen, self.color, self.vertices)

