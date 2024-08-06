import random
import tkinter as tk
from tkinter import messagebox


# Function to get a random word from the predefined list
def get_word():
    words = [
        'python', 'hangman', 'programming', 'openai', 'algorithm',
        'computer', 'science', 'artificial', 'intelligence', 'machine',
        'learning', 'neural', 'network', 'data', 'analysis'
    ]
    return random.choice(words)


# Function to display the hangman image
def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """
    ]
    return stages[tries]


# Function to start the game
def start_game():
    global word, word_completion, guessed, guessed_letters, guessed_words, tries
    word = get_word()
    word_completion = " ".join("_" * len(word))
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    update_display()


# Function to handle guesses
def guess_letter():
    global tries, word_completion, guessed
    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if len(guess) == 1 and guess.isalpha():  # Single letter guess
        if guess in guessed_letters:
            messagebox.showinfo("Hangman", f"You already guessed the letter {guess}")
        elif guess not in word:
            tries -= 1
            guessed_letters.append(guess)
            messagebox.showinfo("Hangman", f"{guess} is not in the word.")
        else:
            guessed_letters.append(guess)
            word_as_list = word_completion.split(" ")
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = " ".join(word_as_list)
            if "_" not in word_completion:
                guessed = True
    elif len(guess) == len(word) and guess.isalpha():  # Whole word guess
        if guess in guessed_words:
            messagebox.showinfo("Hangman", f"You already guessed the word {guess}")
        elif guess != word:
            tries -= 1
            guessed_words.append(guess)
            messagebox.showinfo("Hangman", f"{guess} is not the word.")
        else:
            guessed = True
            word_completion = " ".join(list(word))
    else:
        messagebox.showinfo("Hangman", "Not a valid guess.")

    update_display()

    if guessed:
        messagebox.showinfo("Hangman", "Congrats, you guessed the word! You win!")
        start_game()
    elif tries == 0:
        messagebox.showinfo("Hangman", f"Sorry, you ran out of tries. The word was {word}. Maybe next time!")
        start_game()


# Function to update the display
def update_display():
    hangman_label.config(text=display_hangman(tries))  # Update hangman image
    word_label.config(text=word_completion)  # Update word display
    tries_label.config(text=f"Tries remaining: {tries}")  # Update tries remaining
    guessed_label.config(text=f"Guessed letters: {', '.join(guessed_letters)}")  # Update guessed letters


# Setup the main window
root = tk.Tk()
root.title("Hangman Game")

# Create and pack the labels for hangman image, word, tries, and guessed letters
hangman_label = tk.Label(root, text="", font=("Courier", 18))
hangman_label.pack()

word_label = tk.Label(root, text="", font=("Courier", 18))
word_label.pack()

tries_label = tk.Label(root, text="", font=("Courier", 14))
tries_label.pack()

guessed_label = tk.Label(root, text="", font=("Courier", 14))
guessed_label.pack()

# Create and pack the entry widget and guess button
entry = tk.Entry(root, font=("Courier", 14))
entry.pack()

guess_button = tk.Button(root, text="Guess", command=guess_letter, font=("Courier", 14))
guess_button.pack()

# Start the game for the first time
start_game()

# Run the main loop
root.mainloop()
