import pygame
from pygame.locals import *


class GameObject(pygame.sprite.Sprite):
    def __init__(self, position, collision_rect):
        pygame.sprite.Sprite.__init__(self)

        self.collision_rect = collision_rect
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position
