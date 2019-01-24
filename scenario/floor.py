import pygame
import sys
sys.path.append("../")
from .baseScenario import scenario
from constants import *


class Floor(object):

    def __init__(self, screen=None):
        self.objects = []
        self.color = BLUE
        self.screen = screen

    def set_screen(self, screen):
        self.screen = screen

    def set_color(self, color):
        self.color = color

    # pos, size must be tuples
    def insert(self, pos, size=(GRID_ROW, GRID_COLUMN)):
        self.objects.append(pygame.Rect(pos, size))

    # MAP is a string, with characters that will
    # describe the level map
    def insert_map(self, level_map=scenario):
        for ci, i in enumerate(level_map):
            for cj, j in enumerate(i):
                if j is '#':
                    self.insert(pos=(cj*GRID_ROW, ci*GRID_COLUMN))

    def draw(self):
        for i in self.objects:
            pygame.draw.rect(self.screen, self.color, i)

    def get_scenario(self):
        return self.objects
