import pygame
from .constants import *


class Player(object):

    def __init__(self, pos, size):
        self.rect = pygame.Rect(pos, size)
        self.color = RED
        self.vSpeed = 0
        self.falling = True
        self.screen = None

    def set_color(self, color):
        self.color = color

    def move(self, move_dict, sc):
        colliders = sc.get_scenario()
        if "horizontal" in move_dict:
            if move_dict['horizontal'] == 'left':
                self.move_single_axis(-1, 0, colliders)
            else:
                self.move_single_axis(1, 0, colliders)
        if 'jump' in move_dict:
            if move_dict['jump'] == 'down':
                self.jump(1)
            else:
                self.jump(-1)

    def draw(self, screen=None):
        if screen is None:
            pygame.draw.rect(self.screen, self.color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

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

    def update(self, sc):
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

    def jump(self, direction):
        if not self.falling:
            self.falling = True
            self.vSpeed = JUMP*direction
