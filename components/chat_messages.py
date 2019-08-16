import pygame
from game.game_object import GameObject

GREEN = (53, 204, 53)
RED = (219, 0, 5)


class ChatMessages(GameObject):
    def __init__(self, position, navigator, client):
        GameObject.__init__(self, position)
        self.navigator = navigator
        self.client = client

    def messages(self, screen):
        for index, message in enumerate(self.client.messages):
            font = pygame.font.SysFont('Comic Sans MS', 30)
            text = message[0] + ': ' + message[1]
            text_component = font.render(text, True, RED if message[0] == 'server' else GREEN)
            screen.blit(text_component, (self.position[0] - 200, 80 + (index * 20)))

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
