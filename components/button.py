import pygame
from game.game_object import GameObject


class Button(GameObject):
    def __init__(self, position, size, title, onClick, color=(255, 255, 255)):
        GameObject.__init__(self, position, pygame.Rect(position[0] - size, position[1] - size / 2, size * 2, size))
        self.size = size
        self.color = color
        self.title = title
        self.onClick = onClick

    def set_color(self, new_color):
        self.color = new_color

    def update(self, screen, dt):
        pass

    def on_click(self):
        self.onClick()

    def render(self, screen):
        position = self.get_position()
        size = self.size
        vertices = [(position[0] - size, position[1] - size / 2),
                    (position[0] - size, position[1] + size / 2),
                    (position[0] + size, position[1] + size / 2),
                    (position[0] + size, position[1] - size / 2)]

        pygame.draw.polygon(screen, self.color, vertices)

        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(self.title, True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = self.position

        screen.blit(text, textRect)





