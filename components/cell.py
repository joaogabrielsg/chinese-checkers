import pygame
from game.game_object import GameObject

GREEN = (53, 204, 53)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


class Cell(GameObject):
    def __init__(self, id, color, neighbors, on_click_ref, size=0, line_number=0):
        self.id = id
        self.size = size
        self.color = color
        self.neighbors = neighbors
        self.line_number = line_number
        self.on_click_ref = on_click_ref

    def set_position(self, new_position):
        GameObject.__init__(self, new_position,
                            pygame.Rect(new_position[0] - self.size / 2, new_position[1] - self.size / 2, self.size,
                                        self.size))

    def set_color(self, new_color):
        self.color = new_color

    def update(self, screen, dt):
        pass

    def on_click(self):
        self.on_click_ref(self)

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
