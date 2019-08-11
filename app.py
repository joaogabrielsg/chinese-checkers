from game.game import Game
from containers.table import Table


def main():
    # client = Client('localhost', 65432)
    #
    # client.start_connection()

    game = Game((1200, 700), 'Chinese Checkers', False)
    # pin = Cell((255, 255, 255), (100, 100), 50)
    table = Table((600, 100))

    table.render(game)

    game.start()


if __name__ == "__main__":
    main()
