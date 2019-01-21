from player.player import Player
from player.constants import *
from scenario.floor import Floor
from scenario.baseScenario import scenario
import pygame 

# Init a new player, with position and size as follows.
p1 = Player((10, 10), (10, 10))
# Must be called to initialize pygame stuff;
pygame.init()
# Initializes a screen
screen = pygame.display.set_mode((600, 400))
# The screen is used as an argument so that the
# Floor class can have the "draw" method implemented.
floor = Floor(screen)
# Does the same thing for the player class
p1.set_screen(screen)

# Gets the scenario description (hashes and spaces)
# from the baseScenario file, and inserts it into
# the map
floor.insert_map(scenario)

# Starts the clock, for controlling the frame rate
clock = pygame.time.Clock()

# The game is running.
running = True
while running:

    # Sets the frame rate as 60 fps
    clock.tick(60)
    # For quitting. Losers.
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # This is for playing with controls.
    # The game is intended to be played with scripts,
    # generated through some machine learning/data mining
    # algorithm. This is just for debug and test.
    d = {}
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        d['horizontal'] = 'left'
    if key[pygame.K_RIGHT]:
        d['horizontal'] = 'right'
    if key[pygame.K_UP]:
        d['jump'] = 'up'

    # Does the updates, and drawings.
    p1.move(d, floor)
    p1.update(floor)
    screen.fill(BLACK)
    floor.draw()
    p1.draw()
    pygame.display.flip()
