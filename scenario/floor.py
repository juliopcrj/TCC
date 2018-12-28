import pygame
import sys, os
sys.path.append("../")
from player.constants import *

class Floor(object):

    
    def __init__(self, screen = None):
        self.objects = []
        self.color =  BLUE
        self.screen = screen

    def setScreen(self, screen):
        self.screen = screen

    def setColor(self, color):
        self.color = color

    #pos, size must be tuples
    def insert(self, pos, size=(10,2)):
        self.objects.append(pygame.Rect(pos, size))

    #MAP is a string, with characters that will
    #describe the level map
    def insertMap(self, MAP):
        pass

    def draw(self):
        for i in self.objects:
            pygame.draw.rect(self.screen, self.color, i)

    def getScenario(self):
        return self.objects


