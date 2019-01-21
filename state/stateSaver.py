# This is just a plain "save to csv" thing.
# Could also be done inside the main program, but I
# guess it would make it uglier

import csv


class Save(object):

    def __init__(self, filename='output.csv'):
        self.writer = csv.writer(open(filename, 'r+', newline=''),
                                 delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    def write_state(self, state):
        self.writer.writerow(state)
