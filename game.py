from player.player import Player
from scenario.floor import Floor
from constants import *
import pygame


class Game(object):

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Jump'n Shoot Man")
        self.screen = pygame.display.set_mode((600, 400))
        self.run = True
        self.clock = pygame.time.Clock()
        self.players = []
        self.scenario = Floor(self.screen)

    # @params args: a dictionary of arguments, containing
    # "name", "pos_x"/"pos_y", and "size_x"/"size_y"
    def add_player(self, args):
        self.players.append(Player())
        if "name" in args:
            self.players[-1].set_name(args["name"])
        if "pos_x" in args and "pos_y" in args:
            self.players[-1].set_pos((args["pos_x"], args["pos_y"]))
        if "size_x" in args and "size_y" in args:
            self.players[-1].set_size((args["size_x"], args["size_y"]))
        if "RGB" in args:
            self.players[-1].set_color(args["RGB"])

        self.players[-1].set_screen(self.screen)

    def loop(self):
        while self.run:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.run = False
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    self.run = False
            self.clock.tick(60)

            self.screen.fill(BLACK)
            self.scenario.draw()

            for player in self.players:
                player.update(self.scenario)
                player.draw()

            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.add_player({"name": "1",
                     "pos_x": 2,
                     "pos_y": 2,
                     "RBG": PURPLE})

    game.add_player({"name": "2",
                     "pos_x": 4,
                     "pos_y": 2,
                     "RGB": YELLOW})

    game.scenario.insert_map()

    game.loop()

