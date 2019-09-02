import Pyro4
from connection.rpc_client import Client
from utils.utils import import_file

WHITE = (255, 255, 255)


class GameClient(Client):
    def __init__(self):
        Client.__init__(self, GameClient)
        self.cells = []
        self.messages = []
        self.client_type_turn = 'server'

    def __update_cells(self, id_origin, id_destiny):
        color_origin = self.cells[id_origin].color
        color_destiny = self.cells[id_destiny].color

        self.cells[id_origin].color = color_destiny
        self.cells[id_destiny].color = color_origin

    def move_cell(self, id_origin, id_destiny):
        self.client_type_turn = 'server' if self.client_type == 'client' else 'client'
        self.__update_cells(id_origin, id_destiny)
        self.enemy.__update_cells(id_origin, id_destiny)

    def __new_message(self, message):
        self.messages.append(message)

    def send_message(self, message):
        self.__new_message(message)
        self.enemy.__new_message(message)

    def __on_restart_game(self):
        cell_list = import_file('table_cells.json')
        for cell in cell_list:
            self.cells[cell['id']].color = eval(cell['default_color'])

    def restart_game(self):
        self.__on_restart_game()
        self.enemy.__on_restart_game()

    def __on_close(self):
        self.status_text = 'Adversário desistiu!'
        self.status_type = 0

    def on_close(self):
        self.enemy.__on_close()
        # self.close()

