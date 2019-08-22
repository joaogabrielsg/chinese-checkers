from game.game_object import GameObject
from containers.table import Table
from containers.chat import Chat
from components.button import Button
from components.title import Title
from components.title_turn import TitleTurn


class MainScreen(GameObject):
    def __init__(self, navigator, client):
        self.table = Table((350, 100), navigator, client)
        self.chat = Chat((900, 120), navigator, client)
        self.navigator = navigator
        self.client = client

        self.button = Button((75, 50), 50, 'Sair', self.on_back)
        self.button_restart = Button((75, 150), 50, 'Reiniciar', self.on_restart_game)

    def on_back(self):
        self.client.on_close()
        self.navigator.navigate('start_connection')

    def on_restart_game(self):
        self.client.restart_game()

    def render(self, game):
        game.add_component(self.button)
        game.add_component(self.button_restart)
        game.add_component(Title((600, 40), 100, self.navigator, self.client))

        game.add_component(TitleTurn((600, 600), 100, self.navigator, self.client))

        self.table.render(game)
        self.chat.render(game)
