from random import randint

class Die():
    '''A class representing a single dice'''

    def __init__(self, numSides = 6):

        #initialize the dice
        self.numSides = numSides

    def roll(self):

        #return a random value between 1 and the number of sides
        return randint(1, self.numSides)