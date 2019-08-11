import pygame
from game.game_object import GameObject
from components.cell import Cell


TOTAL_CELLS = 121

#Number of cells in which line
CELLS_IN_LINES = [1, 2, 3, 4, 13, 12, 11, 10, 9, 10, 11, 12, 13, 4, 3, 2, 1]

SPACING_BETWEEN_CELLS = 5

GREEN = (255, 0, 255)
RED = (255, 255, 0)
WHITE = (255, 255, 255)


class Table(GameObject):
    def __init__(self, position):
        GameObject.__init__(self, position)
        self.position = position
        self.cells = []

    @staticmethod
    def render_odd_line(table_center, game, cell_size, line_length, line_height):
        for i in range(line_length):
            game.add_component((Cell(WHITE, (
                ((i - int(line_length / 2)) * (cell_size + SPACING_BETWEEN_CELLS)) + table_center, line_height),
                                     cell_size)))

    @staticmethod
    def render_par_line(table_center, game, cell_size, line_length, line_height):
        for i in range(line_length):
            game.add_component((Cell(WHITE, (
                ((i - int(line_length / 2)) * (cell_size + SPACING_BETWEEN_CELLS)) + table_center + (cell_size/2), line_height),
                                     cell_size)))

    def render(self, game):
        cell_size = 30

        for i in range(TOTAL_CELLS):
            if i <= 10:
                self.cells.append(Cell(GREEN, (100, 100), cell_size))
            elif i > 110:
                self.cells.append(Cell(RED, (100, 100), cell_size))
            else:
                self.cells.append(Cell(WHITE, (100, 100), cell_size))

        for index, line_lenght in enumerate(CELLS_IN_LINES):
            if line_lenght % 2 == 0:
                Table.render_par_line(self.position[0], game, cell_size, line_lenght, (index * cell_size) + self.position[1])
            else:
                Table.render_odd_line(self.position[0], game, cell_size, line_lenght, (index * cell_size) + self.position[1])
