from player.player import Player
from scenario.floor import Floor
from constants import *
from state.stateSaver import Save
from state.stateLoader import Controller #Will use for controlling by file
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
        self.state = {}

    def add_player(self, args):
        """
        This method adds players to the player pool
        :param args: a dictionary, containing indexes "name", "pos_x", "pos_y",
        "size_x", "size_y", "RGB", and "controller".
        :return:
        """
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
            if args['controller'] is 'state_control':
                self.players[-1].set_state(self.state)

        self.players[-1].set_screen(self.screen)

    def save_state(self):
        if len(self.players) is not 2:
            print("Should have 2 players set. Not saving state.")
            return

        players_pos = [self.players[i].rect for i in range(len(self.players))]
        players_facing = [self.players[i].facing for i in range(len(self.players))]
        players_move = [self.players[i].movement for i in range(len(self.players))]
        players_score = [self.players[i].score for i in range(len(self.players))]
        self.state = {
            "p1_x": players_pos[0].x//GRID_COLUMN,
            "p1_y": players_pos[0].y//GRID_ROW,
            "p1_facing": players_facing[0],
            "p1_horizontal": players_move[0]["horizontal"],
            "p1_vertical": players_move[0]["jump"],
            "p1_shoot": players_move[0]["shoot"] or 0,
            "p1_score": players_score[0],
            "p2_x": players_pos[1].x//GRID_COLUMN,
            "p2_y": players_pos[1].y//GRID_ROW,
            "p2_facing": players_facing[1],
            "p2_horizontal":players_move[1]["horizontal"],
            "p2_vertical": players_move[1]["jump"],
            "p2_shoot": players_move[1]["shoot"] or 0,
            "p2_score": players_score[1],
        }
        self.saver.write_state(self.state)

    def loop(self):
        loops = 0
        while self.run:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.run = False
                    self.saver.save_and_quit()
                    return
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    self.run = False
                    self.saver.save_and_quit()
                    return
            self.clock.tick(60)

            self.screen.fill(BLACK)
            self.scenario.draw()

            for player in self.players:
                player.update(self.scenario)
                player.set_state(self.state)
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
                     "controller": "state_control"})
    game.players[-1].set_state_file("inputs.csv")

    game.players[0].add_enemy(game.players[1])
    game.players[1].add_enemy(game.players[0])
    game.scenario.insert_map()

    game.loop()

