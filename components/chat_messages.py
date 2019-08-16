import pygame
from game.game_object import GameObject


class ChatMessages(GameObject):
    def __init__(self, position, navigator, client):
        GameObject.__init__(self, position)
        self.navigator = navigator
        self.client = client

    def messages(self, screen):
        for index, message in enumerate(self.client.messages):
            font = pygame.font.SysFont('Comic Sans MS', 30)
            text = font.render(message, True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (self.position[0], 40 + (index * 20))
            screen.blit(text, text_rect)

    def update(self, screen, dt):
        pass

    def on_click(self):
        pass

    def send_message(self):
        text = self.text_input.get_text()
        self.client.send_message(text)
        self.text_input.text = ''

    def render(self, screen):
        self.messages(screen)
