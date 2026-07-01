#Hangman Game
import random

words = ["apple", "guava", "lemon", "grape", "mango","peach","melon"]
word = random.choice(words)
guessed_word = ["_"] * len(word)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6
print("Welcome to Hangman!")
print(" ".join(guessed_word))
# Step 3: Game loop
while wrong_guesses < max_wrong and "_" in guessed_word:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
        print("Correct!")
    else:
        wrong_guesses += 1
        print(f"Wrong! You have {max_wrong - wrong_guesses} guesses left.")
    print(" ".join(guessed_word))
# Step 4: End game
if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game over! The word was:", word)

