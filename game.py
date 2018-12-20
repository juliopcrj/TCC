from player import Player
import sys, os
import pygame


class Game(object):


    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Jump'n Shoot Man")
        pygame.display.set_mode((600,400))

    def loop(self):
        while self.run:
