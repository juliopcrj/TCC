import pygame
from .constants import *
import sys
sys.path.append("../")
from scenario.floor import Floor

class Player(object):


    def __init__(self, pos, size):
        self.rect = pygame.Rect(pos, size)
        self.color = RED
        self.vSpeed = 0
        self.falling = True

    def setColor(self, color):
        self.color = color

    def move(self, move_dict, sc):
        colliders = sc.getScenario()
        if("horizontal" in move_dict):
            if(move_dict['horizontal'] == 'left'):
                self.move_single_axis(-1,0, colliders)
            else:
                self.move_single_axis(1,0,colliders)
        if('jump' in move_dict):
            if(move_dict['jump'] == 'down'):
                self.jump(1)
            else:
                self.jump(-1)


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    
    def move_single_axis(self,dx,dy,colliders):
        self.rect.x += dx*DELTA_X
        self.rect.y += dy
        collided = False 
        for c in colliders:
            if(self.rect.colliderect(c)):
                collided = True
                if(dx>0):
                    self.rect.right = c.left
                if(dx<0):
                    self.rect.left = c.right
                if(dy > 0):
                    self.rect.bottom = c.top
                if(dy < 0):
                    self.rect.top = c.bottom
        return collided

                    
    def update(self, sc):
        floor = sc.getScenario()
        if(not self.falling):
            standing = False

            for f in floor:
                if(f.top == self.rect.bottom and f.left < self.rect.right and f.right > self.rect.left):
                    standing = True
            self.falling = not standing
        if(self.falling):
            if(not self.move_single_axis(0, self.vSpeed, floor)):
                if(self.vSpeed < MAX_V_SPEED):
                    self.vSpeed += GRAVITY
            else:
                if(self.vSpeed > 0):
                    self.falling = False
                self.vSpeed = 0


    def jump(self, direction):
        if(not self.falling):
            self.falling = True
            self.vSpeed = JUMP*direction


