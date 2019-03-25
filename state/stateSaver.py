# This is just a plain "save to csv" thing.
# Could also be done inside the main program, but I
# guess it would make it uglier

import csv
import os

fieldnames = ['p1_x', 'p1_y', 'p1_facing',
                      'p1_horizontal', 'p1_vertical', 'p1_shoot', 'p1_score',
                      'p2_x', 'p2_y', 'p2_facing',
                      'p2_horizontal', 'p2_vertical', 'p2_shoot', 'p2_score']

# This is file buffering size. To prevent high usage of memory when
# the game is running for a long period... and it seems not to work.
arbitrary_saving_moment = 50


class Save(object):

    def __init__(self, filename='output.csv'):
        exists = filename in os.listdir()
        self.f = open(filename, 'a+', buffering=arbitrary_saving_moment)
        self.writer = csv.DictWriter(self.f, fieldnames=fieldnames)
        if not exists:
            self.writer.writeheader()

    def write_state(self, state):
        self.writer.writerow(state)

    def save_and_quit(self):
        self.f.close()
