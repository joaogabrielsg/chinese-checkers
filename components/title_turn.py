import pygame
from game.game_object import GameObject


class TitleTurn(GameObject):
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
        if self.client.client_type_turn == '':
            title_color = (255, 255, 255)
            title_text = ''
        elif self.client.client_type == self.client.client_type_turn:
            title_color = (53, 204, 53)
            title_text = 'Sua vez'
        else:
            title_color = (219, 0, 5)
            title_text = 'Vez do adversário'

        if self.client.status_type != 0:
            font = pygame.font.SysFont('Comic Sans MS', 40)
            text = font.render('Status: ' + title_text, True, title_color)
            text_rect = text.get_rect()
            text_rect.center = self.position
            screen.blit(text, text_rect)
