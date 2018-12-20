import pygame
from .constants import *

class Player(object):


    def __init__(self, pos, size):
        self.rect = pygame.Rect(pos, size)
        self.color = RED
        self.vSpeed = 0
        self.jumping = True

    def setColor(self, color):
        self.color = color

    def move(self, move_dict, coll):
        if("horizontal" in move_dict):
            if(move_dict['horizontal'] == 'left'):
                self.move_single_axis(-1,0, coll)
            else:
                self.move_single_axis(1,0,coll)
        if('jump' in move_dict):
            if(move_dict['jump'] == 'down'):
                self.jump(1)
            else:
                self.jump(-1)


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    
    def move_single_axis(self,dx,dy,coll):
        self.rect.x += dx*DELTA_X
        self.rect.y += dy
        onFloor = False
        for c in coll:
            if(self.rect.colliderect(c)):
                if(dx>0):
                    self.rect.right = c.left
                else:
                    self.rect.left = c.right
                if(dy > 0):
                    self.rect.bottom = c.top
                    self.jumping = False
                    self.vSpeed = 0
            if(self.rect.bottom == c.top):
                onFloor = True
#        self.jumping = not onFloor

                    
    def update(self, coll):
        #if not jumping, no need to process this update
        if(not self.jumping):
            self.vSpeed = 0
            return
        self.move_single_axis(0,self.vSpeed,coll)
        if(self.vSpeed < MAX_V_SPEED):
            self.vSpeed += GRAVITY
        else:
            self.vSpeed = MAX_V_SPEED
        

    def jump(self, direction):
        if(direction > 0):
            return
        if(not self.jumping):
            self.vSpeed+= direction*JUMP
            self.jumping = True

