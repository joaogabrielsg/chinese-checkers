import pygame
from game.game_object import GameObject


class Title(GameObject):
    def __init__(self, position, size, navigator, client):
        GameObject.__init__(self, position, pygame.Rect(position[0] - size, position[1] - size / 2, size * 2, size))
        self.size = size
        self.navigator = navigator
        self.client = client

    def update(self, screen, dt):
        pass

    def on_click(self):
        pass

    def render(self, screen):
        print(self.client.status_type)
        title_color = (255, 255, 255)
        if self.client.status_type == 0:
            title_color = (255, 255, 255)
        elif self.client.status_type == 1:
            title_color = (53, 204, 53)
        elif self.client.status_type == 2:
            title_color = (219, 0, 5)

        font = pygame.font.SysFont('Comic Sans MS', 40)
        text = font.render('Status: ' + self.client.status_text, True, title_color)
        text_rect = text.get_rect()
        text_rect.center = self.position
        screen.blit(text, text_rect)
