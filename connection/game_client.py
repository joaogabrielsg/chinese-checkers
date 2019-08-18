from connection.client import Client

WHITE = (255, 255, 255)


class GameClient(Client):
    def __init__(self):
        Client.__init__(self, on_receive=self.on_receive)
        self.cells = []
        self.messages = []
        self.client_type_turn = 'server'

    def on_receive(self, object_received):
        if object_received[0] == 'new_message':
            self.__new_message(object_received[1])

        elif object_received[0] == 'move_cell':
            self.client_type_turn = self.client_type
            self.__update_cells(object_received[1][0], object_received[1][1])

    def __update_cells(self, id_origin, id_destiny):
        color_origin = self.cells[id_origin].color
        color_destiny = self.cells[id_destiny].color

        self.cells[id_origin].color = color_destiny
        self.cells[id_destiny].color = color_origin

    def move_cell(self, id_origin, id_destiny):
        self.client_type_turn = 'server' if self.client_type == 'client' else 'client'
        self.__update_cells(id_origin, id_destiny)
        self.send(('move_cell', (id_origin, id_destiny)))

    def __new_message(self, message):
        self.messages.append(message)

    def send_message(self, message):
        self.__new_message(message)
        self.send(('new_message', message))
