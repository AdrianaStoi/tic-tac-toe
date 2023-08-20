
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
