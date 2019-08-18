from game.game_object import GameObject
from components.cell import Cell
import json

TOTAL_CELLS = 121

# Number of cells in which line
CELLS_IN_LINES = [1, 2, 3, 4, 13, 12, 11, 10, 9, 10, 11, 12, 13, 4, 3, 2, 1]

SPACING_BETWEEN_CELLS = 5

GREEN = (53, 204, 53)
RED = (219, 0, 5)
WHITE = (255, 255, 255)
YELLOW = (255, 217, 15)


def import_file(path):
    try:
        json_file = open(path)
        return json.load(json_file)['cells_list']

    except:
        print('Tem um problema com o arquivo JSON.')
        return None


class Table(GameObject):
    def __init__(self, position, navigator, client):
        GameObject.__init__(self, position)
        self.position = position
        self.navigator = navigator
        self.client = client
        self.cell_size = 30
        self.cells_allowed = []

        cell_list = import_file('table_cells.json')

        for cell in cell_list:
            self.client.cells.append(Cell(id=cell['id'],
                                          color=eval(cell['default_color']), neighbors=cell['neighbors'],
                                          on_click_ref=self.on_click, size=self.cell_size))

        self.cell_selected_id = None

    def get_cell_neighbors(self, cell_id):
        return list(filter(lambda cell: cell.id in self.client.cells[cell_id].neighbors, self.client.cells))

    def get_empty_neighbors(self, cell_id):
        return list(filter(lambda cell: cell.color == WHITE, self.get_cell_neighbors(cell_id)))

    def get_occupied_neighbors(self, cell_id):
        return list(filter(lambda cell: cell.color != WHITE, self.get_cell_neighbors(cell_id)))

    def positions_allowed_to_move(self, cell_id):
        self.cells_allowed = self.get_empty_neighbors(cell_id)

    def clean_positions_allowed_to_move(self):
        for cell in self.cells_allowed:
            self.client.cells[cell.id].color = WHITE
        self.cells_allowed = []

    def on_click(self, cell):
        if self.cell_selected_id:
            if cell.color == YELLOW:
                self.clean_positions_allowed_to_move()
                self.client.move_cell(self.cell_selected_id, cell.id)

            self.clean_positions_allowed_to_move()
            self.cell_selected_id = None
        else:
            self.cell_selected_id = cell.id
            self.positions_allowed_to_move(cell.id)
            for cell in self.cells_allowed:
                self.client.cells[cell.id].color = YELLOW

    def render_odd_line(self, game, cells_list, line_height, line_number):
        for index, cell in enumerate(cells_list):
            cell.set_position((
                ((index - int(len(cells_list) / 2)) * (self.cell_size + SPACING_BETWEEN_CELLS)) + self.position[0],
                line_height))
            cell.line_number = line_number

            game.add_component(cell)

    def render_par_line(self, game, cells_list, line_height, line_number):
        for index, cell in enumerate(cells_list):
            cell.set_position((
                ((index - int(len(cells_list) / 2)) * (self.cell_size + SPACING_BETWEEN_CELLS)) + self.position[0] + (
                        self.cell_size / 2), line_height))
            cell.line_number = line_number

            game.add_component(cell)

    def render(self, game):
        line_start_index = 0

        for line_number, line_lenght in enumerate(CELLS_IN_LINES):
            line_cells_list = []

            for line_index in range(line_start_index, line_lenght + line_start_index):
                line_cells_list.append(self.client.cells[line_index])

            if line_lenght % 2 == 0:
                self.render_par_line(game=game,
                                     cells_list=line_cells_list,
                                     line_height=(line_number * self.cell_size) + self.position[1],
                                     line_number=line_number)
            else:
                self.render_odd_line(game=game,
                                     cells_list=line_cells_list,
                                     line_height=(line_number * self.cell_size) + self.position[1],
                                     line_number=line_number)

            line_start_index += line_lenght
