import random

game_instructions = """
Welcome to Tic-Tac-Toe!
Here’s how you can play the game :
o	The game is played on a 3x3 game board.
o	The goal of the game is to form a line of three of your own marks
    horizontally, vertically, or diagonally before the other player.
o	You play the game against the computer.
o	The computer plays using “X”s.
o	You play the game using “O”s.
Good luck!
"""
print(game_instructions)


'''
Asigns the symbols to the computer and the user
'''
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


def check_free_cell(board):
    '''
    Function that checks if cell is free
    '''
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
            print(f"Cell {computer_choice} is already filled in,\
enter a different number.")
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
    Function that asks user about their move,
    checks the validity of user input,
    checks if cell is available and updates the board.
    '''
    print("*** User's turn ***")
    condition = True

    while condition:
        try:
            user_input = int(input("Enter your move\
(only numbers between 1-9 accepted:"))

        except ValueError:
            print("You must enter a number between 1 and 9!")
            continue

        if user_input not in range(1, 10):
            print("Invalid input. Enter a number between 1 and 9")
            continue

        user_position_board = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == user_input:
                    user_position_board = (row, col)

        if user_position_board not in check_free_cell(board):
            print(f"Cell {user_input} is already filled in,\
enter a different number.")
            continue

        row, col = user_position_board
        board[row][col] = "O"
        generate_board(board)

        condition = False

    return check_win(board, computer_symbol, user_symbol)


def check_win(board, computer_symbol, user_symbol):
    '''
    Function that checks for winner on rows, columns and diagonals.
    If there is no winner  and no cells available then winner is "Tie".
    '''
    winner = None

    # Check the winner on rows and columns
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]) and (board[i][0] in [computer_symbol, user_symbol]):  # noqa
            winner = board[i][0]

        if (board[0][i] == board[1][i] == board[2][i]) and (board[0][i] in [computer_symbol, user_symbol]):  # noqa
            winner = board[0][i]

    # Check the winner on diagonals
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] in [computer_symbol, user_symbol]):  # noqa
        winner = board[0][0]

    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][2] in computer_symbol, user_symbol):  # noqa
        winner = board[0][2]

    # Check for tie if there is no winner and if all cells are filled in.
    if not winner and not check_free_cell(board):
        winner = "Tie"

    return winner


while True:
    '''
    The loop will break when the winner is determined
    by the computer_move and user_move functions.
    Appropriate message is printed is the computer or the user is the winner.
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
