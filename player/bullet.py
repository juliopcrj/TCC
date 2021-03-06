import pygame
import sys
sys.path.append("..//")
from constants import *


class Shot(object):
    """
    This class handles the "shots" the players fire.
    TODO: Threading-based parallelism
    """

    def __init__(self, pos, speed, screen, scenario, color):
        self.rect = pygame.Rect(pos, (4, 4))
        self.speed = speed
        self.color = color
        self.screen = screen
        self.scenario = scenario

    def update(self, enemy):
        """
        updates the bullet position, and returns if it collided.
        :param sc: the scenario
        :param screen: a pygame.surface instance
        :return: if the bullet collided in a Scenario element
        """

        self.rect.x += self.speed * BULLET_SPEED
        self.draw()
        if self.rect.colliderect(enemy.rect):
                return True, True
        for tile in self.scenario:
            if self.rect.colliderect(tile):
                return True, False
        return False, False

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
