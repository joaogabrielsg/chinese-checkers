from containers.start_connection import StartConnection
from containers.table import Table


class Navigator:
    def __init__(self, game):
        self.current_page = ''
        self.game = game

    def start_page(self):
        table = StartConnection((600, 200), self)
        table.render(self.game)

    def start_table(self):
        table = Table((600, 100), self)
        table.render(self.game)

    def navigate(self, page):
        self.game.clear_screen()

        if page == 'start_connection':
            self.start_page()

        if page == 'table':
            self.start_table()
