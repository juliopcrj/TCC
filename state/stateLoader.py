import csv
from .constants import MAX_ERROR, RANDOM_TIMER
from random import randint

class Controller(object):

    def __init__(self):
        self.state = []
        self.random_timeout = 0

    def load_states(self, state_file):
        f = open(state_file, 'r')
        fieldnames = ['p1_x', 'p1_y', 'p1_facing',
                      'p1_horizontal', 'p1_vertical', 'p1_shoot', 'p1_score',
                      'p2_x', 'p2_y', 'p2_facing',
                      'p2_horizontal', 'p2_vertical', 'p2_shoot', 'p2_score']
        load_file = csv.DictReader(f, fieldnames=fieldnames)
        for i in load_file:
            self.state.append(i)

        f.close()

        try:
            int(self.state[0]['p1_x'])
        except:
            print("removing first row")
            del(self.state[0])

    def compare_state(self, s, _index):
        # These will be the comparing states. Everything else is command.
        comparable_states = ['p1_x', 'p1_y', 'p2_x', 'p2_y',]
        if s == {}:
            return False
        for i in comparable_states[:4]:
            # TODO: something to leave room for "error" in the match.
            t = type(s[i])
            err = abs(s[i] - t(self.state[_index][i]))
            if(err > MAX_ERROR):
                return False            
        for i in comparable_states[4:]:
            
            if s[i] != self.state[_index][i] and self.state[_index][i] != 0:
                return False
        return True

    def match_state(self, s):
        for i in range(len(self.state)):
            if self.compare_state(s, i):
                print("Matched state\n")
                return i
        return -1

    def random_action(self):
        # User defined random action to happen IF there is no match
        # If user does not implement this, the default random will 
        # happen.
        if self.random_timeout is not 0:
            self.random_timeout -= 1
            return

        self.random_timeout = RANDOM_TIMER
        movement = dict()
        move = randint(-1, 1)
        if move is -1:
            movement['horizontal'] = 'left'
        elif move is 1:
            movement['horizontal'] = 'right'
        else:
            movement['horizontal'] = 'center'

        move = randint(-1, 1)
        if move is -1:
            movement['jump'] = 'up'
        else:
            movement['jump'] = 'not'

        shoot = randint(0, 1)
        movement['shoot'] = shoot
        return movement

    def state_control(self, s):
        _eq = self.match_state(s)
        movement = self.random_action()
        if movement is None:
            return
        if _eq is not -1:
            print("You got a match! Not the one you wanted, though...\n")
            movement['shoot'] = 1
        return movement

