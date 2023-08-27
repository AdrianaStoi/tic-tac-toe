
# Tic-Tac-Toe

Welcome to Tic Tac Toe ! 

Tic-tac-toe, known as noughts and crosses or Xs and Os, is a game designed for two players. They alternate turns to place their designated X or O marks within a 3x3 grid board game. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.
Otherwise, when all cells on the grid are filled and no player has formed a winning line, nobody wins, it is a draw.  

Visit deployed game here : https://my-tic-tac-toe-game-9cab97b48353.herokuapp.com/

![Responsive](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/tic_tac_toe_responsive.png)

---

## Table of contents

- [The goal of the site owner](#the-goal-of-the-site-owner)
- [The goal of the external owner](#the-goal-of-the-external-user)
- [User stories](#user-stories)
- [Flowchart](#flowchart)
- [Features](#features)
    - [Existing Features](#existing-features)
        - [Run Program](#run-program)
        - [Invalid input](#invalid-input)
        - [Winner or Tie](#winner-or-tie)
            - [Winner computer](#winner-computer)
            - [Winner user](#winner-user)
            - [Tie](#tie)
    - [Future features](#future-features)
- [Technology](#technology)
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [User Story Testing](#user-story-testing)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#unfixed-bugs)
    - [Browser Compatibility](#browser-compatibility)
    - [Code validation](#code-validation)
- [Deployment](#deployment)
    - [Codeanywhere](#codeanywhere)
    - [Heroku](#heroku)
- [Credits](#credits)

## The goal of the site owner 

* Provide an entertaining and user-friendly game to the user. Create a game that provides good user experience by applying defensive programming.

## The goal of the external user 

* The user’s goal is to enjoy playing Tic Tac Toe and improve strategic thinking and decision-making skills.

## User stories

* As user, I would like to be able to start or quit the game. 
* As a user, I would like to know the rules of the game.
* As a user, I would like to view updated board and see the available moves. 
* As a user, I would like to see a message displayed, if I enter wrong character.
* As a user, I would like to know how to restart game when it is ended.

[Back to table of contents](#table-of-contents)

---

## Flowchart


* In order to create and plan the game structure, I used [Lucidchart](https://www.lucidchart.com/pages/) to create a flowchart :

![Lucidchart Flowchart-Tic-Tac-Toe](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/flowchart_tic_tac_toe.png)

[Back to table of contents](#table-of-contents)

---

## Features

### Existing Features

#### Run Program

* At the top of the page the user can find the “_Run program_” button which runs the application. 

![Run Program](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/run_program_button.png)

* Once the user clicks on “_Run program_”, they can see “_Welcome to Tic Tac Toe !_” and  the instructions on “_Here’s how you can play the game_”:

![Game instructions](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/game_instructions.png)

* After the game rules section, the user is being asked : "_Type either ‘s’ to start the game or ‘q’ to quit the game._"

    * Typing 's' 

        * If the user types '_s_' the screen is cleared, the game rules are removed. 
        * The user is again informed about the symbols assigned. The computer has the “X” symbol assigned and the user gets the “O” symbol assigned.
        * The computer will add the first random move within the range 1-9, and the board is updated.
        * At the bottom of the game board the user is asked “_Enter your move (only numbers between 1-9 accepted):_”, as per the screenshot below:

    ![Start game](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/type_s.png)

    * Typing 'q'

        * When the user types '_q_' the are prompted with the message :"_Quitting game. Click on 'Run Program' to restart the game._"

    ![Quit game](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/type_q.png)

* The board is being updated with each valid move. The user can see on the board the options available.

![Updated board](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/board_updated.png)

#### Invalid input

* If the user enters any invalid data when he is asked "_Type either ‘s’ to start the game or ‘q’ to quit the game._", they will be prompted with a message “_Invalid input.Enter 's' to start the game or 'q' to quit._" until they enter a valid data. 

![Invalid input when starting or quitting game](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/invalid_input_start_quit.png)

* If the user enters invalid data, e.g. integers greater than 9, they will be prompted with a message “_Invalid input. Enter a number between 1-9._”

![Invalid input for number lesser than 1 and greater than 9](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/invalid_input.png)

* If the user enters letters, other characters, floats, they will be prompted with a message “_You must enter a number between 1-9!_” and he is asked to enter the move:

![Invalid input - characters](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/invalid_characters.png)

![Invalid input - letters](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/invalid_input_letters.png)

![Invalid input - floats](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/invalid_input_floats.png)

* When the user or computer enters a number in a cell that has been already occupied, they will be prompted with a message “_This cell is already filled, enter a different number._”

![Cell already filled-user](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/cell_already_filled_in.png)

![Cell already filled-computer](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/cell_already_filled_in_computer.png)

#### Winner or Tie

* If it’s a win for one of the players, there will be a message displayed: “_Computer won! Play again by clicking on ‘Run Program.’_" or “_You won! Play again by clicking on ‘Run Program.’_"

##### Winner computer

![Winner computer](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/winner_computer.png)

##### Winner user

![Winner user](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/winner_user.png)

##### Tie

* When it’s a tie, meaning all squares on the grid are filled and no player has formed a winning line, the user will see the message: “_It’s a tie! Play again by clicking on ‘Run Program.’_”:

![Tie](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/winner_tie.png)

* The user can start a new game by clicking on "Run program". The user is informed that they can start a new game by clicking on "Run Program" when there is a winner or it’s a tie, as per the screenshots above.

### Future features:

* Provide the option to choose different board sizes.
* Let the user choose the symbol they want.
* Keep score tracking for multiple rounds.

[Back to table of contents](#table-of-contents)

---

## Technology

* I used [Lucidchart](https://www.lucidchart.com/pages/) Flowcharts to create and plan the game structure. The flowchart can be found [here - Tic-Tac-Toe](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/flowchart_tic_tac_toe.pdf).

* I used the editor Codeanywhere for coding. I used Code Institute template. Skillset used for the project was Python. 
* The game was deployed to Heroku and deployment history was maintained through Git commit messages.

[Back to table of contents](#table-of-contents)

---

## Testing

### Manual Testing

* I have tested all functions and features, confirming their proper functionality as expected. The user will encounter error messages at each step when they input data that differs from the required input.

|     Feature       |        Expectation          |        Action        |       Outcome      |
| ----------------- | --------------------------- | -------------------- | ------------------ |
| Run Program button| When clicking on Run Program the game should restart.| Click | When clicking on Run Program the game restarts. ![Run program](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/run_program_button.png)|
| Display game rules  | When the app page is loaded, the game rules should be displayed.| Should be displayed when clicking on Run Program.| When the app page is loaded, the game rules are displayed. ![Game instructions](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/game_instructions.png)|
| Start or quit game feature | When the app page is loaded, underneath the game rules, the user should be prompted to :"_Type 's' to start game or 'q' to quit the game:_"| Function should be called out at the beginning. The text should be displayed when clicking on Run Program.| When the app page is loaded the game rules are displayed and underneath the user can see : "_Type 's' to start game or 'q' to quit the game:_" ![Game instructions](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/game_instructions.png)|
| Start feature – User enters valid data  | When the user types ‘s’, the program should continue to run, and the user should be asked to enter a number between 1-9.| Type valid data ‘s’ | When the user types ‘s’, the program continues to run, and the user is asked to enter a number between 1-9. ![Start game](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/type_s.png)|
| Quit game Feature – User enters valid data | When the user types ‘q’, the user should be prompted with message "_Quitting game. Click on 'Run Program' to restart the game._"| Type valid data ‘q’ | When the user types ‘q’, the user is prompted with the message: "_Quitting game. Click on 'Run Program' to restart the game._"![Quit game](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/type_q.png)|
| Start or quit game feature – invalid data  | When the user enters any invalid data, _e.g. other letters, special characters, any numbers_, the error message should be displayed until they enter a valid input:  "_Invalid input. Enter 's' to start the game or 'q' to quit._" | Type invalid data | When the user enters any invalid data, _e.g. other letters, special characters, any numbers_, they are prompted with the error message until they enter a valid input: "_Invalid input. Enter 's' to start the game or 'q' to quit._" ![Invalid input when starting or quitting game](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/invalid_input_start_quit.png)|
| Computer’s turn  | After the user enters ‘s’ to start the game, the computer should execute its initial random move by selecting a number between 1-9. This move should subsequently update the game board.  | Once user enters valid data to start game ‘s’, computer should make a random move within the range 1-9.| Once the user enters ‘s’ to initiate the game, the computer executes its initial random move by selecting a number between 1-9 and the board game is updated accordingly. ![Game instructions](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/game_instructions.png) |
| User’s turn – valid data  | Once the computer executes the move, the message "_Enter your move, (only numbers between 1-9 accepted:)_" should be displayed. If the user inputs valid data, the board should be updated, followed by the computer’s turn.| After the computer’s turn, the user should be prompted to enter valid data. Type number between 1-9| When the computer executes the move, the message "_Enter your move,(only numbers between 1-9 accepted:)_" is being displayed. When the user inputs valid data, the board is updated, followed by the computer’s turn. ![User move](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/user_turn_message.png)|
| User’s turn – any invalid data type | When the user enters any invalid data, when trying to make a move, _e.g. integers greater than 9 and less than 1_, they should be prompted with a message “_Invalid input. Enter a number between 1-9._” When the user enters other invalid data,  letters, other characters, floats, they should be prompted with the message. “_You must enter a number between 1-9!_” and then to be asked to enter the move.| Type invalid data. Number outside the range 1-9 or any other character, letter. | When the user enters any invalid data, when trying to make a move, _e.g. integers greater than 9 and less than 1_, they are prompted with a message “_Invalid input. Enter a number between 1-9._” ![Invalid input for number lesser than 1 and greater than 9](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/invalid_input.png) When the user enters other invalid data,  letters, other characters, floats, they are prompted with the message. “_You must enter a number between 1-9!_” and then they are asked to enter the move.![Invalid input - characters](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/invalid_characters.png) ![Invalid input - letters](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/invalid_input_letters.png) ![Invalid input - floats](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/invalid_input_floats.png) |
| Input a move into a cell already occupied - user or computer  | When user or computer chooses a number in a cell that is already filled in, an error message should be displayed: “_Cell (user or computer input) is already filled in, enter a different number._” | Type number in the range 1-9 | When the user or computer chooses a number in a cell that is already filled in, an error message is displayed:  “_Cell (user or computer input) is already filled in, enter a different number._” ![Cell already filled-user](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/cell_already_filled_in.png) ![Cell already filled-computer](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/cell_already_filled_in_computer.png)|
| Winner on rows  | When either symbol ‘X’ (computer) or ‘O’ (user) forms a line on any of the three rows, a message should be printed with the corresponding message: “_Computer won!Play again by clicking on 'Run Program.'_” or “_You won!Play again by clicking on 'Run Program'._” | Either ‘X’ or ‘O’ forms a line in any of the three rows | When either symbol ‘X’ (computer) or ‘O’ (user) forms a line on any of the three rows, a message is printed with the corresponding message: “_Computer won!Play again by clicking on 'Run Program'._” or “_You won!Play again by clicking on 'Run Program'._” ![winner computer](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/winner_computer.png) |
| Winner on columns | When either symbol ‘X’ (computer) or ‘O’ (user) forms a line on any of the three columns, a message should be printed with the corresponding message: “_Computer won!Play again by clicking on 'Run Program'._” or “_You won!Play again by clicking on 'Run Program'._” | Either ‘X’ or ‘O’ forms a line in any of the three columns | When either symbol ‘X’ (computer) or ‘O’ (user) forms a line on any of the three columns, a message is printed with the corresponding message: “_Computer won!_” or “_You won!_” ![winner user](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/winner_user.png)  ![winner user](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagestesting/winner_on_column_middle_user.png) |
| Winner on diagonals  | TWhen either symbol ‘X’ (computer) or ‘O’ (user) forms a line on any of the two diagonals, a message should be printed with the corresponding message: “_Computer won!Play again by clicking on 'Run Program'._” or “_You won!Play again by clicking on 'Run Program'._” | Either ‘X’ or ‘O’ forms a line in any of the two diagonals| When either symbol ‘X’ (computer) or ‘O’ (user) forms a line on any of the two diagonals, a message is printed with the corresponding message: “_Computer won!Play again by clicking on 'Run Program'._” or “_You won!Play again by clicking on 'Run Program'._” ![winner diagonal user](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagestesting/winner_on_diagonal_user.png)  ![winner diagonal computer](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagestesting/winner_on_diagonal_computer.png)|
| Tie  | If all cells are filled in with ‘X’ and ‘O’ and there is no line formed, then it is a tie. The message : "_It's a tie. Play again by clicking on 'Run Program'._" it is displayed. | All cells are filled in with ‘X’ and ‘O’ without forming a line. | Once all cells are filled in with ‘X’ and ‘O’ and there is no line formed, then it is a tie. The message: "_It's a tie. Play again by clicking on 'Run Program'._" it is displayed. ![Tie](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagesreadme/winner_tie.png)|

### User Story Testing

|                User Story                            |                                            Testing                                                         |
|------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
|As a user, I would like to know the rules of the game.| <ul><li>The game rules are displayed in the terminal, when you click on the Heroku app link or when you click on “_Run Program_”.</li></ul>|
|As user, I would like to be able to start or quit the game.| <ul><li>After the game rules, you are being asked to type either ‘s’ to start the game or ‘q’ to quit the game.If you enter invalid data, you receive an error message until you enter the requested valid data.</li></ul>|
|As a user, I would like to view updated board and see the available moves.| <ul><li>The game board is updated after each user and computer move. The board is displayed in the terminal. The numbers from 1-9 are displayed. When you or computer enters a move the numbers are replaced with “X” and “O”.</li></ul>|
|As a user, I would like to see a message displayed, if I enter wrong character.| <ul><li>You are prompted with a message every time you enter an invalid input, _e.g. letters, special characters, integers less than 1 or greater than 9_.</li></ul>|
|As a user, I would like to know how to restart game when it is ended.| <ul><li>When the game ends, meaning you win, computer wins or when is a tie, you are prompted with the message: “_Play again by clicking on ‘Run Program.'_”</li></ul>|

### Fixed Bugs

* User was asked only once to enter input. The while loop would only go once and not continue the game.
* The problem was the indentation of “_condition= False_”. Fixed indentation for “_condition = False_”, as per below:

![Bug asking for user input only once](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagestesting/bug_asking_for_user_input_only_once.png)  ![Fixed bug indentation of condition false](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagestesting/fixed_bug_indentation_of_condition_false.png)

* When it was a tie, there were two messages displayed: “_It’s a tie_” and “_Computer won_”.
* Fixed bug by adding an “_if/else_” condition under the while loop when there is a winner, as per below:

![Bug two messages appear when tie](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagestesting/bug_two_messages_appear_when_tie.png)  ![Solved bug tie one message displayed](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagestesting/solved_bug_tie_one_message_displayed.png)

### Unfixed Bugs
I am not aware of any remaining unresolved bugs.

### Browser Compatibility

* I tested the site on different browsers Google Chrome, Edge and Mozilla. The game functions worked properly on all tested browsers.

### Code validation

* The _run.py_ file successfully passed through the [PEP8 CI](https://pep8ci.herokuapp.com/#) validator without any errors being detected.

![PEP8 validator](https://github.com/AdrianaStoi/tic-tac-toe/blob/main/documentation/imagestesting/code_validation_tic_tac_toe.png)

[Back to table of contents](#table-of-contents)

---

## Deployment

### Codeanywhere

* I used Codenywhere to create and run the project. Here are the steps to create the workspace and run the project:
  * Log in to Codeanywhere using GitHub account: https://app.codeanywhere.com/
  * On the Dashboard, click on “_New Workspace_” which can be found under “_Workspaces_” section.
  * Copy and paste the Repository URL created in GitHub (by using the Code Institute p3-template) into the designated field.
  * Click on "_Create_".
  * New Workspace is created in Codeanywhere.
  * To run and view the project written in Codeanywhere, click on “_Terminal_” in the upper bar, then select “_New Terminal_”.
  * The New terminal will open at the bottom part of the page. To run the application, type “_python3 run.py_” in the terminal.
  * The preview application will run in the terminal in Codeanywhere.

### Heroku

To deploy the project on Heroku the following steps were followed: 

* Log into [Heroku](https://heroku.com/) account 
* From the Heroku dashboard click on “_New_” on the upper right corner and then click on “_Create new app_”
* Add app name (app name must be unique on Heroku)
* Then select the appropriate region e.g. “_Europe_” and then click on “_Create app_”
* Go to “_Settings tab_”
* Go to "_Config Vars_" and under KEY type "_PORT_" and under Value type "_8000_"
* Then go to to “_Buildpacks_” section located after the “_Confirg Vars_” section, making sure the two packages are added in this order:
    * Click on “_Add Buildpack_”, then select “_heroku/python_” and click on “_Add Buildpack_”
    * Then select “_heroku/nodejs_” and click on “_Add Buildpack_” 
* Next go to “_Deploy_” tab located at the top of the page
* Under “_Deployment method_” section, select Github here, and then confirm connection to Github 
* Search for the corresponding Github repository name, _e.g. tic-tac-toe_ and click “_Search_” 
* Click on “_Connect_” to link up the Heroku app to the GitHub repository code
* Scroll down on the page, and there are two deployment options in this section: “_Automatic deploys_” and “_Manual deploy_”
* Under “_Manual deploy_”, click on “_Deploy Branch_”
* Once is deployed there is a message displayed “_Your app was successfully deployed._” And a button “_View_” 
* Click on “_View_” and you are directed to the app deployed and the link

Visit deployed game here : https://my-tic-tac-toe-game-9cab97b48353.herokuapp.com/

[Back to table of contents](#table-of-contents)

---

## Credits

* For the game description I used as source [Wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe).
* I used [Code Institute - Template](https://github.com/Code-Institute-Org/python-essentials-template) for the deployable application.
* For Flowchart creation I used [Lucidchart](https://www.lucidchart.com/).
* To create generate board function, I used  as source the blog article of [Hamza El Yaaqouobi](https://helyaaqoubi.gitlab.io/coding/2020/05/12/tic-tac-toe-coding.html)
which was customized and I adapted it accordingly.
* I created the check for win function by following [Stackflow thread](https://stackoverflow.com/questions/74379382/cs50-ai-tic-tac-toe-player-x-has-3-in-a-row-yet-doesnt-win-o-picks-next-a-3) and project of [Pam Qian](https://gist.github.com/qianguigui1104/edb3b11b33c78e5894aad7908c773353) which were used as guidance. I customized and adapted the function accordingly.
* To create the clear()function, to facilitate UX experience and clear screen, I used as source the  thread on [slack](https://app.slack.com/client/T0L30B202/C027C3S3TEU/thread/C027C3S3TEU-1646215428.957489) and the code to create function was taken from the [blog article on Scaler](https://www.scaler.com/topics/how-to-clear-screen-in-python/).
* To create quit game function I used code from [Freecodecamp](https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/).

[Back to table of contents](#table-of-contents)