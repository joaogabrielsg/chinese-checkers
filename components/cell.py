import pygame
from game.game_object import GameObject


GREEN = (53, 204, 53)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


class Cell(GameObject):
    def __init__(self, color, position, size, neighbors, line_number):
        GameObject.__init__(self, position, pygame.Rect(position[0] - size / 2, position[1] - size / 2, size, size))
        self.size = size
        self.color = color
        self.neighbors = neighbors
        self.line_number = line_number

    def set_color(self, new_color):
        self.color = new_color

    def update(self, screen, dt):
        pass

    def on_click(self):
        if self.color == GREEN:
            self.set_color(RED)
        else:
            self.set_color(GREEN)

    def render(self, screen):
        position = self.get_position()
        size = self.size
        vertices = [(position[0], position[1] - size / 2),
                    (position[0] - size / 2, position[1] - size / 2.5),
                    (position[0] - size / 2, position[1] + size / 2.5),
                    (position[0], position[1] + size / 2),
                    (position[0] + size / 2, position[1] + size / 2.5),
                    (position[0] + size / 2, position[1] - size / 2.5)]

        pygame.draw.polygon(screen, self.color, vertices)




