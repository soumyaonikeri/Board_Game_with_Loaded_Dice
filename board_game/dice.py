import random

class LoadedDice:
    def __init__(self):
        self.probabilities = [1] * 4 + [2] * 2 + [3] * 2 + ["RollAgain"] * 2

    def roll(self):
        return random.choice(self.probabilities)
