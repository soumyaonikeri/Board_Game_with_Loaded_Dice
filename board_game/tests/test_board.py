import unittest
from board_game.board import Board
from board_game.player import Player

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board("HHBJHHHHJHHBHHHHBHHHJJHHHHHJHBH")
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")

    def test_move_player(self):
        print("Testing move_player...")
        input("Press Enter to continue...")
        print(f"Initial position: {self.player1.position}")
        self.board.move_player(self.player1, 2, [self.player1, self.player2])
        print(f"New position: {self.player1.position}")
        self.assertEqual(self.player1.position, 2)

    def test_land_on_bank(self):
        print("Testing land_on_bank...")
        input("Press Enter to continue...")
        self.player1.position = 3
        initial_balance = self.player1.balance
        print(f"Initial balance: {initial_balance}")
        self.board.land_on_bank(self.player1)
        print(f"New balance after landing on bank: {self.player1.balance}")
        self.assertEqual(self.player1.balance, initial_balance + 10)

    def test_land_on_jail(self):
        print("Testing land_on_jail...")
        input("Press Enter to continue...")
        self.player1.position = 3
        initial_balance = self.player1.balance
        print(f"Initial balance: {initial_balance}")
        self.board.land_on_jail(self.player1)
        print(f"New balance after landing on jail: {self.player1.balance}")
        self.assertEqual(self.player1.balance, initial_balance - 20)
        self.assertTrue(self.player1.miss_turn)

    def test_land_on_house(self):
        print("Testing land_on_house...")
        input("Press Enter to continue...")
        self.player1.position = 0
        initial_balance = self.player1.balance
        initial_debt = self.player1.debt
        print(f"Initial balance: {initial_balance}, Initial debt: {initial_debt}")
        self.board.land_on_house(self.player1, [self.player1, self.player2])
        print(f"New balance after landing on house: {self.player1.balance}")
        print(f"New debt after landing on house: {self.player1.debt}")
        if initial_balance > 0:
            self.assertEqual(self.player1.balance, initial_balance + 2)
        elif initial_balance < 0:
            self.assertEqual(self.player1.balance, initial_balance - 2)
        else:
            self.assertEqual(self.player1.balance, initial_balance)
        if initial_debt > 0:
            self.assertEqual(self.player1.debt, initial_debt + 1)
        else:
            self.assertEqual(self.player1.debt, initial_debt)

if __name__ == "__main__":
    unittest.main()
