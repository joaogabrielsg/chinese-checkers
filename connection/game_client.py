from connection.client import Client


class GameClient(Client):
    def __init__(self):
        Client.__init__(self, on_receive=self.on_receive)
        self.cells = []
        self.messages = []

    def on_receive(self, object_received):
        if object_received[0] == 'new_message':
            self.__new_message(object_received[1])

        elif object_received[0] == 'move_cell':
            self.__update_cells(object_received[1][0], object_received[1][1])

    def __change_cells_colors(self, cell, id_origin, id_destiny):
        # color_origin = filter(lambda cell_from_cells: True if cell_from_cells.id == id_origin else False, self.cells)[
        #     0].color
        # color_destiny = filter(lambda cell_from_cells: True if cell_from_cells.id == id_destiny else False, self.cells)[
        #     0].color
        color_origin = (53, 204, 53)
        color_destiny = (255, 255, 255)
        if cell.id == id_origin or cell.id == id_destiny:
            if cell.id == id_origin:
                new_cell = cell
                new_cell.color = color_destiny
                return new_cell
            elif cell.id == id_destiny:
                new_cell = cell
                new_cell.color = color_origin
                return new_cell
        else:
            return cell

    def __update_cells(self, id_origin, id_destiny):
        self.cells = map(lambda cell: self.change_cells_colors(cell, id_origin, id_destiny), self.cells)

    def move_cell(self, id_origin, id_destiny):
        print(id_origin, id_destiny)
        self.__update_cells(id_origin, id_destiny)
        self.send(('move_cell', (id_origin, id_destiny)))

    def __new_message(self, message):
        self.messages.append(message)

    def send_message(self, message):
        self.__new_message(message)
        self.send(('new_message', message))
