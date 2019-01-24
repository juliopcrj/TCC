# This is just a plain "save to csv" thing.
# Could also be done inside the main program, but I
# guess it would make it uglier

import csv
import os


class Save(object):

    def __init__(self, filename='output.csv'):
        exists = filename in os.listdir()
        f = open(filename, 'a+')
        fieldnames = ['p1_x', 'p1_y', 'p1_facing',
                      'p1_horizontal', 'p1_vertical', 'p1_shoot', 'p1_score',
                      'p2_x', 'p2_y', 'p2_facing',
                      'p2_horizontal', 'p2_vertical', 'p2_shoot', 'p2_score']
        if not exists:
            self.writer = csv.DictWriter(f, fieldnames=fieldnames)

    def write_state(self, state):
        self.writer.writerow(state)
