from .board import Board
from .player import Player
from .dice import LoadedDice


class Game:
    def __init__(self, board_layout):
        self.board = Board(board_layout)
        self.players = [Player("Player 1"), Player("Player 2")]
        self.dice = LoadedDice()
        self.current_player_index = 0

    def display_board(self):
        board_display = list(self.board.layout)
        for player in self.players:
            board_display[player.position] = player.name[0]
        print("".join(board_display))

    def display_status(self):
        for player in self.players:
            print(f"{player.name} - Balance: {player.balance}, Debt: {player.debt}, Position: {player.position}")

    def play_turn(self):
        player = self.players[self.current_player_index]
        if player.can_play():
            self.display_status()
            self.display_board()

            input(f"{player.name}, press Enter to roll the dice...")
            dice_result = self.dice.roll()
            while dice_result == "RollAgain":
                print(f"{player.name} rolled 'Roll Again'. Rolling again...")
                dice_result = self.dice.roll()

            print(f"{player.name} rolled a {dice_result}")
            self.board.move_player(player, dice_result, self.players)

            # Handle optional actions like loan and repayment if the player is on a bank square
            current_square = self.board.layout[player.position]
            if current_square == 'B':
                self.handle_bank_options(player)

        self.current_player_index = (self.current_player_index + 1) % 2

    def handle_bank_options(self, player):
        while True:
            choice = input(
                f"{player.name}, you landed on a bank! Choose an option:\n1. Take a loan\n2. Repay debt\n3. Do nothing\nEnter your choice: ")
            if choice == '1':
                max_loan = 10 * player.balance
                loan_amount = int(input(f"Enter loan amount (up to {max_loan}): "))
                if 0 <= loan_amount <= max_loan:
                    player.balance += loan_amount
                    player.debt += loan_amount
                    break
                else:
                    print("Invalid loan amount.")
            elif choice == '2':
                repayment_amount = int(input("Enter repayment amount: "))
                if 0 <= repayment_amount <= player.balance:
                    player.balance -= repayment_amount
                    player.debt -= repayment_amount
                    break
                else:
                    print("Invalid repayment amount.")
            elif choice == '3':
                break
            else:
                print("Invalid choice.")

    def check_win_conditions(self):
        for player in self.players:
            if player.balance - player.debt > 100:
                print(f"{player.name} wins with a balance of {player.balance} and debt of {player.debt}!")
                return True
            opponent = player.opponent(self.players)
            if opponent.debt - opponent.balance > 100:
                print(f"{player.name} wins as the opponent {opponent.name} has a debt exceeding balance by 100!")
                return True
        return False

    def start(self):
        while not self.check_win_conditions():
            self.play_turn()
