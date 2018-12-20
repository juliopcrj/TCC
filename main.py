from player.player import Player
from player.constants import *
import pygame 

p1 = Player((10,10),(10,10))
pygame.init()
screen = pygame.display.set_mode((600,400))
floor = pygame.Rect((0,380),(600,20))
clock = pygame.time.Clock()



running = True
while(running):

    clock.tick(60)
    for e in pygame.event.get():
        if(e.type == pygame.QUIT):
            running = False
        if(e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            running = False


    key = pygame.key.get_pressed()
    if(key[pygame.K_LEFT]):
        p1.move({'horizontal':'left'}, [floor])
    if(key[pygame.K_RIGHT]):
        p1.move({'horizontal':'right'}, [floor])

    p1.update([floor])
    screen.fill(BLACK)
    p1.draw(screen)
    pygame.draw.rect(screen, BLUE, floor)
    pygame.display.flip()
