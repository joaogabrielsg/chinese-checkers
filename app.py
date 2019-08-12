import pygame
from game.game import Game
from containers.table import Table
from containers.start_connection import StartConnection


def main():
    pygame.font.init()
    game = Game((1200, 700), 'Chinese Checkers', False)

    # client = Client('localhost', 65432)
    #
    # client.start_connection()

    table = StartConnection((600, 200))

    table.render(game)

    # table = Table((600, 100))
    #
    # table.render(game)

    game.start()


if __name__ == "__main__":
    main()
