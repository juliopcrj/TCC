import pygame
import sys
sys.path.append("../")
from constants import *
from random import randint
from .bullet import Shot


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

    def shoot(self):
        if self.cooldown is 0:
            speed = -1 if self.facing is "left" else 1
            self.shots.append(Shot(self.rect.center), speed)
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
            else:
                self.jump(-1)

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

    def update(self, sc, enemy_shots=[]):
        """
        Updates (almost) every detail of the player instance
        :param sc: the scenario to process the colisions
        :param enemy_shots: a list of shots. This is obtained from Player.shots.
        :return: nothing.
        """
        if self.alive:
            floor = sc.get_scenario()
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

        for bullet in self.shots:
            if bullet.update():
                self.shots.remove(bullet)

    def die(self):
        self.alive = False
        self.respawn_time = 1

    def respawn(self):
        self.alive = True
        self.set_pos((randint() % GRID_COLUMN, randint() % GRID_ROW))

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
    # TODO: Make a 'select' controls method, for defining weather it's controlled by human or machine
