import random
import os
import sys


def clear_screen():
    '''
    Function that clears the screen.
    This code was taken from :
    https://www.scaler.com/topics/how-to-clear-screen-in-python/
    '''
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


clear_screen()


def quit_game():
    '''Function that exists the game.'''
    sys.exit(0)


GAME_INSTRUCTIONS = """
Welcome to Tic-Tac-Toe!
Here's how you can play the game :
o	The game is played on a 3x3 game board.
o	The goal of the game is to form a line of three of your own marks
    horizontally, vertically, or diagonally before the other player.
o	You play the game against the computer.
o	The computer plays using “X”s.
o	You play the game using “O”s.
o   If you want to restart game click on "Run Program".
Good luck!
"""


def display_instructions():
    '''Function that prints the game instructions.'''
    print(GAME_INSTRUCTIONS)


display_instructions()


def start_game():
    '''
    Function that prompts the user to tpe 's' to start the game.
    It checks data validity, otherwise error message received.
    '''

    while True:
        print("Type 's' to start game or 'q' to quit the game.")
        start_input = input()
        if start_input == 's':
            break
        elif start_input == 'q':
            print("Quitting game.")
            quit_game()
            break
        else:
            print("Invalid input. Enter 's' to start the game or 'q' to quit.")
    clear_screen()


start_game()


computer_symbol = "X"
user_symbol = "O"
symbols = computer_symbol, user_symbol
print(f"Computer's symbol is: {symbols[0]}")
print(f"Your symbol is: {symbols[1]}")

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def generate_board(board):
    '''Creates the board and displays board number inside the cells.'''
    print("\n" + "+-----" * len(board[0]) + "+")
    for row in board:
        print("|     " * 3, "|", sep="")
        print("|" + "|".join(f"{str(cell).center(5)}" for cell in row) + "|")
        print("|     " * 3, "|", sep="")
        print("+" + "+".join("-----" for _ in row) + "+")
    print()


generate_board(board)


def check_free_cell(board):
    '''Function that checks if cell is free.'''
    available_cell = []
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] not in ["X", "O"]:
                available_cell.append((row, column))

    return available_cell


def computer_move(board):
    '''
    Adds computer random choice between 1 and 9,
    checks the validity of computer input,
    checks if cell is available and updates the board.
    '''
    condition = True
    while condition:
        computer_choice = random.randint(1, 9)
        computer_position_board = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == computer_choice:
                    computer_position_board = (row, col)
        if computer_position_board not in check_free_cell(board):
            print(f"Cell {computer_choice} is already filled in,", end=" ")
            print("enter a different number.")
            continue
        else:
            print("Computer's move:", computer_choice)
        row, col = computer_position_board
        board[row][col] = "X"
        generate_board(board)
        condition = False
    return check_win(board, computer_symbol, user_symbol)


def user_move(board):
    '''
    Function that asks user about their move.
    While loop, while true checks the validity of user input,
    checks if cell is available and updates the board.
    '''
    print("*** Your turn ***")
    condition = True
    while condition:
        try:
            print("Enter your move", end=" ")
            print("(only numbers between 1-9 accepted:)", end=" ")
            user_input = int(input())
        except ValueError:
            print("You must enter a number between 1 and 9!")
            continue
        if user_input not in range(1, 10):
            print("Invalid input. Enter a number between 1 and 9.")
            continue
        user_position_board = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == user_input:
                    user_position_board = (row, col)
        if user_position_board not in check_free_cell(board):
            print(f"Cell {user_input} is already filled in,", end=" ")
            print("enter a different number.")
            continue
        row, col = user_position_board
        board[row][col] = "O"
        generate_board(board)
        condition = False
    return check_win(board, computer_symbol, user_symbol)


def check_win(board, computer_symbol, user_symbol):
    '''
    Function that checks for winner on rows, columns and diagonals.
    For loop with if statements checks winner on row and columns.
    The following 2 if statements outside loop checks winner on diagonals
    Last if statement, if there is no winner and no cells available,
    then winner is "Tie".
    '''
    winner = None
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]):
            if (board[i][0] in [computer_symbol, user_symbol]):
                winner = board[i][0]
        if (board[0][i] == board[1][i] == board[2][i]):
            if (board[0][i] in [computer_symbol, user_symbol]):
                winner = board[0][i]
    if (board[0][0] == board[1][1] == board[2][2]):
        if (board[0][0] in [computer_symbol, user_symbol]):
            winner = board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]):
        if (board[0][2] in computer_symbol, user_symbol):
            winner = board[0][2]

    if not winner and not check_free_cell(board):
        winner = "Tie"
    return winner


while True:
    '''
    The loop will break when the winner is determined.
    It alternates between the computer_move and user_move
    and checks for the winner or tie after each move.
    Appropriate message is printed if the computer, user is the winner
    or it's tie.
    '''
    winner = computer_move(board)
    if winner:
        if winner == "Tie":
            print("It's a tie. Play again by clicking on 'Run Program'.")
        else:
            print("Computer won!Play again by clicking on 'Run Program'.")
        break
    winner = user_move(board)
    if winner:
        if winner == "Tie":
            print("It's a tie. Play again by clicking on 'Run Program'.")
        else:
            print("You won!Play again by clicking on 'Run Program'.")
        break
