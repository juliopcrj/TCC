from player.player import Player
from player.constants import *
from scenario.floor import Floor
from scenario.baseScenario import scenario
import pygame 

p1 = Player((10,10),(10,10))
pygame.init()
screen = pygame.display.set_mode((600,400))
floor = Floor(screen)

level = [
    "##########",
    "#        #",
    "#        #",
    "#        #",
    "#        #",
    "#        #",
    "#     ####",
    "#        #",
    "##########"
]

floor.insertMap(scenario)
#floor.insert((-100,180),(800,20))
#floor.insert((100, 160), (30, 5))
clock = pygame.time.Clock()



running = True
while(running):

    clock.tick(60)
    for e in pygame.event.get():
        if(e.type == pygame.QUIT):
            running = False
        if(e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            running = False

    d = {}
    key = pygame.key.get_pressed()
    if(key[pygame.K_LEFT]):
        d['horizontal'] = 'left'
    if(key[pygame.K_RIGHT]):
        d['horizontal'] = 'right'
    if(key[pygame.K_UP]):
        d['jump'] = 'up'

    p1.move(d, floor)
    p1.update(floor)
    screen.fill(BLACK)
    floor.draw()
    p1.draw(screen)
    pygame.display.flip()
