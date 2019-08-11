import pygame
from game.game_object import GameObject


class Cell(GameObject):
    def __init__(self, color, position, size):
        GameObject.__init__(self, position, pygame.Rect(position[0] - size / 2, position[1] - size / 2, size, size))
        self.size = size
        self.color = color

    def set_color(self, new_color):
        self.color = new_color

    def update(self, screen, dt):
        pass

    def on_click(self):
        self.set_color((255, 0, 255))

    def render(self, screen):
        position = self.get_position()
        size = self.size
        vertices = [(position[0], position[1] - size / 2),
                    (position[0] - size / 2, position[1] - size / 3),
                    (position[0] - size / 2, position[1] + size / 3),
                    (position[0], position[1] + size / 2),
                    (position[0] + size / 2, position[1] + size / 3),
                    (position[0] + size / 2, position[1] - size / 3)]

        return pygame.draw.polygon(screen, self.color, vertices)




