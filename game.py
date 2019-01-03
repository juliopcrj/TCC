from player.player import Player
from scenario.floor import Floor
import sys, os
import pygame


class Game(object):

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Jump'n Shoot Man")
        pygame.display.set_mode((600, 400))
        self.run = True

    def loop(self):
        clock = pygame.time.Clock()
        while self.run:
            for e in pygame.event.get():
                if(e.type == pygame.QUIT):
                    self.run = False
                if(e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                    self.run = False
            #Write rest of code below this line


if __name__ == "__main__":
    game = Game()
    game.loop()

