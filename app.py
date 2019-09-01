import pygame
from game.game import Game
from router.navigation import Navigator


def main():
    pygame.font.init()
    game = Game((1200, 650), 'Chinese Checkers', False)

    navigator = Navigator(game)
    # navigator.navigate('start_connection')
    navigator.navigate('main_screen')

    game.start()


if __name__ == "__main__":
    main()
