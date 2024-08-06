# Hangman Game

This is a simple Hangman game implemented in Python using the Tkinter library for the graphical user interface.

## Features

- Random word selection from a predefined list of words.
- Graphical display of the hangman as the game progresses.
- User input for guessing letters or the whole word.
- Display of guessed letters and remaining tries.
- Message boxes to inform the user about the game status (win/lose).

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)

## Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory.

## Usage

1. Run the `Hangman.py` file to start the game:
    ```sh
    python Hangman.py
    ```
2. A window will open displaying the hangman game interface.
3. Enter your guesses in the input field and click the "Guess" button.

## Code Overview

- `get_word()`: Function to get a random word from a predefined list.
- `display_hangman(tries)`: Function to display the hangman image based on the number of tries left.
- `start_game()`: Function to initialize and start a new game.
- `guess_letter()`: Function to handle the user's guesses.
- `update_display()`: Function to update the game display based on the current game state.

## License

This project is licensed under the MIT License.