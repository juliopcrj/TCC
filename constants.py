# Constants

# Physics stuff
DELTA_X     = 2 #Horizontal Movement
GRAVITY     = 1 #Vertical gravity
JUMP        = 10    #Starting jump speed
MAX_V_SPEED = 10
BULLET_SPEED = 8


# Let's play with colors :)
BLACK    = (0,0,0)
WHITE    = (255,255,255)
RED      = (255,0,0)
BLUE     = (0,0,255)
GREEN    = (0,255,0)
YELLOW   = (255,255,0)
PURPLE   = (128,0,128)
FUCSIA   = (255,0,255)
GRAY     = (128,128,128)
AQUA     = (0,255,255)


# Screen stuff

GRID_ROW    = 10
GRID_COLUMN = 10

# Game Stuff
SAVE_FRAME = 15     # how many frames until save the state
SHOT_COOLDOWN = 45  # how much time to wait until being able to fire again
MAX_SHOTS = 1       # how many shots each player can have currently on screen
RESPAWN_TIME = 60   # how much time until respawn
RANDOM_TIMER = 60   # time for the random movement choser to stick to that movement

# State comparisson stuff
MAX_ERROR = 3 # Error in measurement, in map squares
