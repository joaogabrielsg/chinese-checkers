import pygame
from game.game_object import GameObject


class Button(GameObject):
    def __init__(self, position, size, title, onClick, color=(255, 255, 255)):
        GameObject.__init__(self, position, pygame.Rect(position[0] - size, position[1] - size / 2, size * 2, size))
        self.size = size
        self.color = color
        self.title = title
        self.onClick = onClick

        self.vertices = [(position[0] - size, position[1] - size / 2),
                         (position[0] - size, position[1] + size / 2),
                         (position[0] + size, position[1] + size / 2),
                         (position[0] + size, position[1] - size / 2)]

        font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text = font.render(self.title, True, (0, 0, 0))
        self.textRect = self.text.get_rect()
        self.textRect.center = self.position

    def set_color(self, new_color):
        self.color = new_color

    def update(self, screen, dt):
        pass

    def on_click(self):
        self.onClick()

    def render(self, screen):
        pygame.draw.polygon(screen, self.color, self.vertices)
        screen.blit(self.text, self.textRect)
