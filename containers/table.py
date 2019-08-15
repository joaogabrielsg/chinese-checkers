import json
from game.game_object import GameObject
from components.cell import Cell

TOTAL_CELLS = 121

# Number of cells in which line
CELLS_IN_LINES = [1, 2, 3, 4, 13, 12, 11, 10, 9, 10, 11, 12, 13, 4, 3, 2, 1]

SPACING_BETWEEN_CELLS = 5

GREEN = (53, 204, 53)
RED = (219, 0, 5)
WHITE = (255, 255, 255)


class Table(GameObject):
    def __init__(self, position, navigator, client):
        GameObject.__init__(self, position)
        self.position = position
        self.cells = []
        self.navigator = navigator
        self.client = client

    def render_odd_line(self, game, cell_size, cells_list, line_height, line_number):
        for index, cell in enumerate(cells_list):
            cell = Cell(eval(cell['default_color']), (
                ((index - int(len(cells_list) / 2)) * (cell_size + SPACING_BETWEEN_CELLS)) + self.position[0],
                line_height),
                        cell_size, cell['neighbors'], line_number)

            self.cells.append(cell)
            game.add_component(cell)

    def render_par_line(self, game, cell_size, cells_list, line_height, line_number):
        for index, cell in enumerate(cells_list):
            cell = Cell(eval(cell['default_color']), (
                ((index - int(len(cells_list) / 2)) * (cell_size + SPACING_BETWEEN_CELLS)) + self.position[0] + (
                        cell_size / 2),
                line_height), cell_size, cell['neighbors'], line_number)

            self.cells.append(cell)
            game.add_component(cell)

    @staticmethod
    def import_file(path):
        try:
            json_file = open(path)
            return json.load(json_file)['cells_list']

        except:
            print('Tem um problema com o arquivo JSON.')
            return None

    def render(self, game):
        cell_size = 30
        line_start_index = 0
        cells_list = Table.import_file('table_cells.json')

        for line_number, line_lenght in enumerate(CELLS_IN_LINES):
            line_cells_list = []

            for line_index in range(line_start_index, line_lenght + line_start_index):
                line_cells_list.append(cells_list[line_index])

            if line_lenght % 2 == 0:
                self.render_par_line(game, cell_size, line_cells_list, (line_number * cell_size) + self.position[1],
                                     line_number)
            else:
                self.render_odd_line(game, cell_size, line_cells_list, (line_number * cell_size) + self.position[1],
                                     line_number)

            line_start_index += line_lenght
