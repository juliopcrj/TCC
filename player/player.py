import pygame
import sys
import math
sys.path.append("../")
from constants import *
from random import randint
from .bullet import Shot
from state.stateLoader import Controller


class Player(object):

    """
    Player is the base character in the game.
    """
    def __init__(self, pos=(10, 10), size=(10, 10)):
        """
        Creates a new "Player" instance.
        :param pos: a tuple containing the x,y coordinates of the top-left part of the rectangle.
        :param size: the x,y size in pixels.
        """
        self.rect = pygame.Rect(pos, size)
        self.color = RED
        self.vSpeed = 0
        self.falling = True
        self.facing = "left"
        self.screen = None
        self.name = ""
        self.controller = None
        self.shots = []
        self.cooldown = 0
        self.alive = True
        self.respawn_time = 0
        self.movement = {}
        self.random_timeout = 0
        self.score = 0
        self.state_controller = None
        self.state = None
        self.enemy = None 

    def add_enemy(self, enemy):
        self.enemy = enemy

    def shoot(self, sc):
        if self.cooldown is 0:
            speed = -1 if self.facing is "left" else 1
            self.shots.append(Shot(self.rect.center, speed, self.screen, sc))
            self.cooldown = 1

    def set_name(self, name):
        self.name = name

    def set_pos(self, pos):
        x, y = pos
        self.rect.left, self.rect.top = x*GRID_ROW, y*GRID_COLUMN

    def set_size(self, size):
        self.rect.width, self.rect.height = size

    def set_color(self, color):
        self.color = color

    def move(self, move_dict, sc):
        colliders = sc.get_scenario()
        if "horizontal" in move_dict:
            if move_dict['horizontal'] == 'left':
                self.move_single_axis(-1, 0, colliders)
                self.facing = "left"
            else:
                self.move_single_axis(1, 0, colliders)
                self.facing = "right"
        if 'jump' in move_dict:
            if move_dict['jump'] == 'down':
                self.jump(1)
            elif move_dict['jump'] == 'up':
                self.jump(-1)
        if "shoot" in move_dict:
            if move_dict['shoot'] == 1:
                self.shoot(colliders)

    def draw(self, screen=None):
        if self.alive:
            scr = self.screen or screen
            pygame.draw.rect(scr, self.color, self.rect)

    def set_screen(self, screen):
        self.screen = screen

    def move_single_axis(self, dx, dy, colliders):
        self.rect.x += dx*DELTA_X
        self.rect.y += dy
        collided = False
        for c in colliders:
            if self.rect.colliderect(c):
                collided = True
                if dx > 0:
                    self.rect.right = c.left
                if dx < 0:
                    self.rect.left = c.right
                if dy > 0:
                    self.rect.bottom = c.top
                if dy < 0:
                    self.rect.top = c.bottom
        return collided

    def get_shots(self):
        """

        :return: the "shots" list.
        """
        return self.shots

    def update(self, sc, enemy_shots=[], move_dict=None):
        """
        Updates (almost) every detail of the player instance
        :param sc: the scenario to process the colisions
        :param enemy_shots: a list of shots. This is obtained from Player.shots.
        :param move_dict: a dictionary of movements. that dictionary is described in the help.md.
        :return: nothing.
        """
        if self.alive:
            move = None
            floor = sc.get_scenario()
            if self.controller is "state_control":
                move = self.state_controller.state_control(self.state)
            if move is None or self.controller is "random":
                self.random_movement()

            self.movement = move_dict or self.movement or move
            self.move(self.movement, sc)

            if not self.falling:
                standing = False

                for f in floor:
                    if f.top == self.rect.bottom and f.left < self.rect.right and f.right > self.rect.left:
                        standing = True
                self.falling = not standing
            if self.falling:
                if not self.move_single_axis(0, self.vSpeed, floor):
                    if self.vSpeed < MAX_V_SPEED:
                        self.vSpeed += GRAVITY
                else:
                    if self.vSpeed > 0:
                        self.falling = False
                    self.vSpeed = 0
            if self.cooldown is not 0:
                self.cooldown += 1
            if self.cooldown is SHOT_COOLDOWN:
                self.cooldown = 0

            if len(enemy_shots) is not 0:
                for shot in enemy_shots:
                    if self.rect.colliderect(shot.rect):
                        self.die()
                        enemy_shots.remove(shot)
        else:
            if self.respawn_time is RESPAWN_TIME:
                self.respawn()
            else:
                self.respawn_time += 1

        for bullet in self.shots:
            res = bullet.update(self.enemy)
            if res[0]:
                self.shots.remove(bullet)
            if res[1]:
                self.kill()

    def kill(self ):
        self.enemy.die()
        self.score += 1

    def die(self):
        self.alive = False
        self.respawn_time = 0

    def respawn(self):
        self.alive = True
        self.set_pos((randint(1,GRID_COLUMN-1), randint(1, GRID_ROW-1)))

    def jump(self, direction):
        if not self.falling:
            self.falling = True
            self.vSpeed = JUMP*direction

    """
    Sets the controller, defined by the user. The controller can be either a keyboard input, or am
    automated controller, like a script-based controller.
    """
    def set_controller(self, controller):
        """
        :param controller: the controller that should be used.
        :return: nothing
        """
        self.controller = controller
        if self.controller is "state_control":
            self.state_controller = Controller()

    def set_state_file(self, file):
        self.state_controller.load_states(file)

    def random_movement(self):
        if self.random_timeout is not 0:
            self.random_timeout -= 1
            return

        self.random_timeout = RANDOM_TIMER
        self.movement = dict()
        move = randint(-1, 1)
        if move is -1:
            self.movement['horizontal'] = 'left'
        elif move is 1:
            self.movement['horizontal'] = 'right'
        else:
            self.movement['horizontal'] = 'center'

        move = randint(-1, 1)
        if move is -1:
            self.movement['jump'] = 'up'
        else:
            self.movement['jump'] = 'not'

        shoot = randint(0, 1)
        self.movement['shoot'] = shoot

    def set_state(self, state):
        self.state = state

    def rudimentary_ai_movement(self, rest=None):
        """
        This method defines a simple "ai" moving behavior
        It basically makes the player follow the other one
        :param rest: a list of the other players
        :return: nothing.
        """
        if self.random_timeout is not 0:
            self.random_timeout -= 1
            return

        self.random_timeout = RANDOM_TIMER
        self.movement = dict()

    def get_closest_enemy(self, rest=None):
        """
        Gets the closest enemy to the current player, in order
        to be used in tht rudimentary_ai_movement.
        :param rest: a list of the other players
        :return: the closest enemy, if any. If none, then None.
        """
        if not rest:
            return None
        distance = self.get_distance(self.rect, rest[0].rect)
        curr_enemy = rest[0]
        for enemy in rest:
            d = self.get_distance(self.rect, enemy.rect)
            if d < distance:
                distance = d
                curr_enemy = enemy

        return curr_enemy

    @staticmethod
    def get_distance(object_a, object_b):
        return math.hypot(object_a.centerx - object_b.centerx, object_a.centery - object_b.centery)

