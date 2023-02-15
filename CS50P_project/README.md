# CS50 Mastermind
#### Video Demo:  <https://www.youtube.com/watch?v=WbjwWdiR8kI>
#### Description:
CS50 Mastermind is a command line game that allows the user to guess a randomly generated combination of colours, much like the classic board game. The player has eight attempts to guess the correct sequence of colours. The game will provide feedback after each guess, indicating the number of correctly positioned colours and the number of colours that are correct but in the wrong position. The game also includes a difficulty selection feature, where the player can choose from three difficulty levels. This difficulty level slider will increase the number of colours to guess while keeping the number of attempts constant. The colour combinations are selected from the following colours: R (Red), G (Green), B (Blue), Y (Yellow), W (White), and P (Purple). The game is created in Python and uses the logging module for debugging purposes.

#### How to use:
1. Run the program by executing the main() function in the terminal.
2. The game will introduce itself and provide the rules.
3. The player will be asked to choose a difficulty level from 1 to 3.
4. The game will generate a secret combination of colours based on the selected difficulty level.
5. The player will have eight attempts to guess the colour combination by entering the first letter of each colour and pressing space.
6. After each guess, the game will provide feedback by indicating the number of correctly positioned colours and the number of colours that are correct but in the wrong position.
7. If the player guesses the correct colour combination, the game will congratulate them, and the number of attempts will be displayed.
8. If the player does not guess the correct colour combination within the eight attempts, the game will reveal the correct sequence of colours.

#### Files:
project.py: This file contains the Python code for the CS50 Mastermind game.
test_project.py: This file contains the test cases for the CS50 Mastermind game.

#### Requirements:
Python 3.x
Logging module
Mock module

#### Breakdown:
There were a couple of key design choices made throughout this project. The first was the implementation of the logging module. Rather than scatter the codebase with comments that would then need to be commented out or removed later, I researched the logging module. It has the ability to provide meaningful print statements, but can be easily removed by changing the master logging level in one location. This saved me a lot of time while refactoring my code.

The other key design decision came from issues passing one of the unit tests. What was originally an all-in-one input and validation function turned into moving the while loop and input call outside of the function into main() and transforming the function to be strictly for validating. This allowed me to keep the functionality of the code while also simplifying this key function and test case.