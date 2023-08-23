
# Tic-Tac-Toe

Welcome to Tic Tac Toe ! 

Tic-tac-toe, known as noughts and crosses or Xs and Os, is a game designed for two players. They alternate turns to place their designated X or O marks within a 3x3 grid board game. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.
Otherwise, when all cells on the grid are filled and no player has formed a winning line, nobody wins, it is a draw.  

Visit deployed game here : https://my-tic-tac-toe-game-9cab97b48353.herokuapp.com/

![Responsive](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/tic_tac_toe_responsive.png)

## Site owner's goal:

* Provide an entertaining and user-friendly game to the user. Create a game that provides good user experience by applying defensive programming.

## External user’s goal:

* The user’s goal is to enjoy playing Tic Tac Toe and improve strategic thinking and decision-making skills.

## User stories:

* As a user, I would like to know the rules of the game.
* As a user, I would like to view updated board and see the available moves. 
* As a user, I would like to see a message displayed, if I enter wrong character.
* As a user, I would like to know how to restart game when it is ended.

## Features

### Existing Features

#### Run Program

* At the top of the page the user can find the “Run program” button which runs the application. 

![Run Program](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/run_program_button.png)

* Once the user clicks on “Run program”, they can see “Welcome to Tic Tac Toe !” and  the instructions on “Here’s how you can play the game”:

![Game instructions](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/game_instructions.png)

* The computer has the “X” symbol assigned and the user gets the “O” symbol assigned.

![Game symbols](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/symbols_assigned.png)

* Underneath the game rules the board is displayed. The computer makes the first move. Computer will add a random move within the range 1-9.

![Computer move](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/computer_move.png)

* At the bottom of the game board the user is asked “Enter your move (only numbers between 1-9 accepted):”

![User move](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/user_turn_message.png)

* The board is being updated with each move. The user can see on the board the options available.

![Updated board](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/board_updated.png)

#### Invalid input

* If the user enters invalid data, e.g. integers greater than 9, they will be prompted with a message “Invalid input. Enter a number between 1-9.”

![Invalid input for number lesser than 1 and greater than 9](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/invalid_input.png)

* If the user enters letters, other characters, floats, they will be prompted with a message “You must enter a number between 1-9!” and he is asked to enter the move:

![Invalid input - characters](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/invalid_characters.png)

![Invalid input - letters](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/invalid_input_letters.png)

![Invalid input - floats](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/invalid_input_floats.png)

* When the user or computer enters a number in a cell that has been already occupied, they will be prompted with a message “This cell is already filled, enter a different number.”

![Cell already filled-user](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/cell_already_filled_in.png)

![Cell already filled-computer](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/cell_already_filled_in_computer.png)

#### Winner or Tie

* If it’s a win for one of the players, there will be a message displayed: “Computer won! Play again by clicking on ‘Run Program.’ or “You won! Play again by clicking on ‘Run Program.’

##### Winner computer

![winner computer](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/winner_computer.png)

##### Winner user

![winner user](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/winner_user.png)

##### Tie

* When it’s a tie meaning all squares on the grid are filled and no player has formed a winning line, the user will see the message: “It’s a tie! Play again by clicking on ‘Run Program.’:”

![tie](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/winner_tie.png)

* The user can start a new game by clicking on ‘Run program’. The user is informed that they can start a new game by clicking on ‘Run Program’ when there is a winner or it’s a tie, as per the screenshots above.

### Future features:

* Provide the option to choose different board sizes.
* Let the user choose the symbol they want.
* Keep score tracking for multiple rounds.

### Technology

* I used [Lucidchart](https://www.lucidchart.com/pages/) Flowcharts to create and plan the game structure. The flowchart can be found [here - Tic-Tac-Toe](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/flowcharts_tic_tac_toe.pdf).

![Lucid Flowchart-Tic-Tac-Toe](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/flowchart_tic_tac_toe.png)

* I used the editor Codeanywhere for coding. I used Code Institute template. Skillset used for the project was Python. 
* The game was deployed to Heroku and deployment history was maintained through Git commit messages.

### Testing

#### Fixed Bugs

* User was asked only once to enter input. The while loop would only go once and not continue the game.
* The problem was the indentation of “condition= False”. Fixed indentation for “condition = False”, as per below:

![Bug asking for user input only once](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagestesting/bug_asking_for_user_input_only_once.png) ![Fixed bug indentation of condition false](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagestesting/fixed_bug_indentation_of_condition_false.png)

* When it was a tie there were two messages displayed “It’s a tie” and “Computer won”.
* Fixed bug by adding an “if/else” condition under the while loop when there is a winner, as per below:

![Bug two messages appear when tie](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagestesting/bug_two_messages_appear_when_tie.png) ![Solved bug tie one message displayed](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagestesting/solved_bug_tie_one_message_displayed.png)

## Browser Compatibility

* I tested the site on different browsers Google Chrome, Edge and Mozilla. The game functions worked properly on all tested browsers.

## Code validation

* The run.py file successfully passed through the [PEP8]( https://pep8ci.herokuapp.com/#) official validator without any errors being detected.