import pygame
import sys
sys.path.append("..//")
from constants import *


class Shot(object):
    """
    This class handles the "shots" the players fire.
    TODO: Threading-based parallelism
    """

    def __init__(self, pos, speed, screen, scenario):
        self.rect = pygame.Rect(pos, (2, 2))
        self.speed = speed
        self.color = FUCSIA
        self.screen = screen
        self.scenario = scenario

    def update(self):
        """
        updates the bullet position, and returns if it collided.
        :param sc: the scenario
        :param screen: a pygame.surface instance
        :return: if the bullet collided in a Scenario element
        """

        self.rect.x += self.speed * BULLET_SPEED
        self.draw()
        for tile in self.scenario:
            if self.rect.colliderect(tile):
                return True
        return False

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
