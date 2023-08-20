import random

game_instructions = """
Welcome to Tic-Tac-Toe!
Here’s how you can play the game :
o	The game is played on a 3x3 game board.
o	The goal of the game is to form a line of three of your own marks
    horizontally, vertically, or diagonally before the other player.
o	You play the game against the computer.
o	The computer plays using “X”s.
o	You play the game using “0”s.
Good luck!
"""
print(game_instructions)


def players_symbols():
    '''
    Asigns the symbols to the computer and the user
    '''
    computer_symbol = "X"
    user_symbol = "0"
    return computer_symbol, user_symbol


computer_symbol, user_symbol = players_symbols()

print(f"Computer's symbol is: {computer_symbol}")
print(f"Your symbol is: {user_symbol}")

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def generate_board(board):
    '''
    Creates the board and displays board number inside the cells. 
    The cells may be accessed using board[row][column]
    '''
    print(f"""\n 
    +-----+-----+-----+
    |     |     |     |
    |{str(board[0][0]).center(5)}|{str(board[0][1]).center(5)}|{str(board[0][2]).center(5)}|
    |     |     |     |
    +-----+-----+-----+
    |     |     |     |
    |{str(board[1][0]).center(5)}|{str(board[1][1]).center(5)}|{str(board[1][2]).center(5)}|
    |     |     |     |
    +-----+-----+-----+
    |     |     |     |
    |{str(board[2][0]).center(5)}|{str(board[2][1]).center(5)}|{str(board[2][2]).center(5)}|
    |     |     |     |
    +-----+-----+-----+\n
    """)

generate_board(board)


def computer_move(board):
    '''
    Add computer random choice between 1 and 9.
    '''
    return random.randint(1,9)

computer_choice = computer_move(board)
print("Computer's move:", computer_choice)