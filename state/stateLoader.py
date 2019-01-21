import csv


class Controller(object):

    def __init__(self):
        self.state = []

    def load_states(self, state_file):
        f = open(state_file, 'r')
        load_file = csv.reader(f)
        for i in load_file:
            self.state.append(i)

    def compare_state(self, s, _index):
        for i in range(len(s)):
            if s[i] != self.state[_index][i]:
                return False
        return True

    def match_state(self, s):
        for i in range(len(self.state)):
            if self.compare_state(s, i):
                return i
        return -1

    def random_action(self):
        # User should define a method for
        # what the player will do when no
        # states match the current.
        pass

    def state_control(self, s):
        _eq = self.match_state(s)
        if _eq is -1:
            return self.random_action()
        move = {'horizontal': self.state[_eq]['horizontal'],
                'vertical': self.state[_eq]['vertical'],
                'shoot': self.state[_eq]['shoot']}
        return move

