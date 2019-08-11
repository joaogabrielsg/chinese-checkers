import pygame
from game.game_object import GameObject


GREEN = (0, 128, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

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
        if self.color == GREEN:
            self.set_color(RED)
        else:
            self.set_color(GREEN)

    @staticmethod
    def render_component(screen, color, position, size):
        cell = Cell(color, position, size)
        cell.render(screen)

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




