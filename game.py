from player.player import Player
from scenario.floor import Floor
from constants import *
from state.stateSaver import Save
from state.stateLoader import Controller
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
        self.saver = Save()
        self.controllers = []

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
        if "controller" in args:
            self.players[-1].set_controller(args["controller"])

        self.players[-1].set_screen(self.screen)

    def save_state(self):
        if len(self.players) is not 2:
            print("Should have 2 players set. Not saving state.")
            return
        players_pos = [self.players[i].rect for i in range(len(self.players))]
        players_facing = [self.players[i].facing for i in range(len(self.players))]
        state = {
            "p1_x": players_pos[0].x//GRID_COLUMN,
            "p1_y": players_pos[0].y//GRID_ROW,
            "p1_facing": players_facing[0],
            "p1_horizontal": 0,
            "p1_vertical": 0,
            "p1_shoot": 0,
            "p1_score": 0,
            "p2_x": players_pos[1].x//GRID_COLUMN,
            "p2_y": players_pos[1].y//GRID_ROW,
            "p2_facing": players_facing[1],
            "p2_horizontal": 0,
            "p2_vertical": 0,
            "p2_shoot": 0,
            "p2_score": 0,
        }
        self.saver.write_state(state)

    def loop(self):
        loops = 0
        while self.run:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.run = False
                    self.saver.save_and_quit()
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    self.run = False
                    self.saver.save_and_quit()
            self.clock.tick(60)

            self.screen.fill(BLACK)
            self.scenario.draw()

            for player in self.players:
                player.update(self.scenario)
                player.draw()

            pygame.display.flip()
            loops = loops + 1
            if loops is SAVE_FRAME:
                loops = 0
                self.save_state()


if __name__ == "__main__":
    game = Game()
    game.add_player({"name": "1",
                     "pos_x": 2,
                     "pos_y": 2,
                     "RBG": PURPLE,
                     "controller": "random"})

    game.add_player({"name": "2",
                     "pos_x": 4,
                     "pos_y": 2,
                     "RGB": YELLOW,
                     "controller": "random"})

    game.scenario.insert_map()

    game.loop()

