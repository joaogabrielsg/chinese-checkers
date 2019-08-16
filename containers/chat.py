from game.game_object import GameObject
from components.button import Button
from components.text_input import TextInput
from components.chat_messages import ChatMessages


class Chat(GameObject):
    def __init__(self, position, navigator, client):
        GameObject.__init__(self, position)
        self.navigator = navigator
        self.client = client

        self.button = Button((self.position[0] + 100, self.position[1] + 400), 50, 'Enviar', self.send_message)
        self.text_input = TextInput((self.position[0] - 100, self.position[1] + 400), 100)
        self.chat_messages = ChatMessages((self.position[0] + 100, self.position[1]), self.navigator, self.client)

    def send_message(self):
        text = self.text_input.get_text()
        self.client.send_message(text)
        self.text_input.text = ''

    def render(self, game):
        game.add_component(self.text_input)
        game.add_component(self.button)
        game.add_component(self.chat_messages)
