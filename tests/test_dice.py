import unittest
from board_game.dice import LoadedDice

class TestLoadedDice(unittest.TestCase):
    def setUp(self):
        self.dice = LoadedDice()

    def test_roll(self):
        print("Testing roll...")
        input("Press Enter to continue...")
        result = self.dice.roll()
        print(f"Dice rolled: {result}")
        self.assertIn(result, [1, 2, 3, "RollAgain"])

if __name__ == "__main__":
    unittest.main()
