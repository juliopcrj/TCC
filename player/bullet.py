import pygame
import sys
sys.path.append("..//")
from constants import *


class Shot(object):
    """
    This class handles the "shots" the players fire.
    TODO: Threading-based paralelism
    """

    def __init__(self, pos, speed):
        self.rect = pygame.Rect(pos, (1, 1))
        self.speed = speed
        self.color = FUCSIA

    def update(self, sc=None, screen=None):
        """
        updates the bullet position, and returns if it collided.
        :param sc: the scenario
        :param screen: a pygame.surface instance
        :return: if the bullet collided in a Scenario element
        """
        if sc is not None:
            self.rect.x += self.speed * BULLET_SPEED
            self.draw(screen)
            for tile in sc:
                if self.rect.colliderect(tile):
                    return True
            return False
        return True

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
