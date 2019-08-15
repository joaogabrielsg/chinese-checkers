from containers.start_connection import StartConnection
from containers.main_screen import MainScreen
from connection.client import Client


class Navigator:
    def __init__(self, game):
        self.current_page = ''
        self.game = game
        self.client = Client()

    def start_page(self):
        table = StartConnection((600, 200), self, self.client)
        table.render(self.game)

    def start_main_screen(self):
        main_screen = MainScreen(self, self.client)
        main_screen.render(self.game)

    def navigate(self, page):
        self.game.clear_screen()

        if page == 'start_connection':
            self.start_page()

        if page == 'main_screen':
            self.start_main_screen()
