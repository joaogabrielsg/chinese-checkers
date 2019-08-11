from connection.client import Client
from game.game import Game
from components.cell import Cell


def main():
    # client = Client('localhost', 65432)
    #
    # client.start_connection()

    game = Game((400, 400), 'teste', False)
    pin = Cell((255, 255, 255), (100, 100), 50)

    game.add_component(pin)

    game.start()


if __name__ == "__main__":
    main()
