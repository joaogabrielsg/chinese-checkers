import pygame
from pygame.locals import *


class Game:
    def __init__(self, size, title, fullscreen=True):

        pygame.init()
        flags = DOUBLEBUF
        if fullscreen:
            flags |= FULLSCREEN
        self.screen = pygame.display.set_mode(size, flags)

        self.background_color = 17, 16, 24
        self.screen_size = self.screen.get_size()
        self.run = None
        self.components = []

        pygame.display.set_caption(title)

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type in (KEYDOWN, KEYUP):
                k = event.key

            if event.type == QUIT:
                self.run = False

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_components = [component for component in self.components if component.collision_rect.collidepoint(pos)]
                for component in clicked_components:
                    component.on_click()

            elif event.type == KEYDOWN:
                if k == K_ESCAPE:
                    self.run = False

    def __components_render(self):
        for component in self.components:
            component.render(self.screen)

    def __components_update(self):
        events = pygame.event.get()
        for component in self.components:
            component.update(self.screen, events)

    def start(self):
        # frames por segundo do jogo
        clock = pygame.time.Clock()

        self.run = True
        while self.run:
            # clock.tick(1000 / dt)

            self.screen.fill(self.background_color)
            self.__components_update()
            self.__handle_events()
            self.__components_render()

            # ao fim do desenho temos que trocar o front buffer e o back buffer
            # pygame.display.flip()

            # print("FPS: %0.2f" % clock.get_fps())

            pygame.display.update()
            clock.tick(30)

    def stop(self):
        self.run = False

    def add_component(self, component):
        self.components.append(component)
