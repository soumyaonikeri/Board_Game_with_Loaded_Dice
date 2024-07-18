# Circular Board Game

## Introduction
This is a two-player circular board game implemented in Python. Players roll a loaded dice to move around a board consisting of various squares such as Banks, Jails, and Houses. The goal is to achieve a net balance of more than 100 or make the opponent's net debt exceed 100.

## Requirements
- Python 3.x

## How to Run
1. Clone the repository:
    ```sh
    git clone https://github.com/soumyaonikeri/Board_Game_with_Loaded_Dice.git
    ```
2. Run the game:
    ```sh
    python main.py
    ```

## Assumptions
- The board layout is predefined in the code.
- The game runs in a command-line interface.
- Inputs and interactions are handled through text prompts.

## Tests
Unit tests are provided for the board, player, and dice functionalities. To run the tests:
```sh
python -m unittest discover -s tests
```
#To test each file seperately run following commands
```sh
python -m unittest tests/test_board.py
```
```sh
python -m unittest tests/test_dice.py
```
```sh
python -m unittest tests/test_player.py
```



