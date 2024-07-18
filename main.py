from board_game.game import Game

def main():
    board_layout = "HHBJHHHHJHHBHHHHBHHHJJHHHHHJHBH"
    game = Game(board_layout)
    game.start()

if __name__ == "__main__":
    main()
