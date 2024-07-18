import unittest
from board_game.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Player 1")

    def test_initial_balance_and_debt(self):
        print("Testing initial_balance_and_debt...")
        input("Press Enter to continue...")
        print(f"Initial balance: {self.player.balance}, Initial debt: {self.player.debt}")
        self.assertEqual(self.player.balance, 5)
        self.assertEqual(self.player.debt, 0)

    def test_miss_turn(self):
        print("Testing miss_turn...")
        input("Press Enter to continue...")
        self.player.miss_turn = True
        initial_miss_turn = self.player.miss_turn
        print(f"Initial miss turn status: {initial_miss_turn}")
        self.assertFalse(self.player.can_play())
        print(f"New miss turn status after can_play(): {self.player.miss_turn}")
        self.assertFalse(self.player.miss_turn)

    def test_opponent(self):
        print("Testing opponent...")
        input("Press Enter to continue...")
        player2 = Player("Player 2")
        print(f"Player 1's opponent: {self.player.opponent([self.player, player2]).name}")
        self.assertEqual(self.player.opponent([self.player, player2]), player2)

if __name__ == "__main__":
    unittest.main()
