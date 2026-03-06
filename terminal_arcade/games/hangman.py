import random
import json
from utils import title


def play():

    title("HANGMAN")

    try:
        with open("words.json") as f:
            word_data = json.load(f)
        words = word_data.get("hangman", [])
        if not words:
            print("❌ Error: No hangman words found in words.json")
            return
    except FileNotFoundError:
        print("❌ Error: words.json file not found!")
        print("Please ensure words.json is in the terminal_arcade directory.")
        return
    except json.JSONDecodeError:
        print("❌ Error: words.json is not valid JSON!")
        return

    word = random.choice(words)
    guessed = []
    tries = 6

    print("\n✍️  Guess the word! You have 6 tries.")
    print("Wrong guesses: ", end="")

    while tries > 0:

        display = ""

        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "

        print(f"\n\nWord: {display}")
        print(
            f"Guessed letters: {', '.join(sorted(guessed)) if guessed else 'None'}")
        print(f"Tries remaining: {tries}")

        if "_" not in display:
            print(f"\n✅ Congratulations! You found the word: {word}")
            return

        while True:
            guess = input("\nGuess a letter: ").lower().strip()
            if len(guess) != 1 or not guess.isalpha():
                print("❌ Please enter a single letter.")
                continue
            if guess in guessed:
                print(f"❌ You already guessed '{guess}'.")
                continue
            break

        if guess in word:
            guessed.append(guess)
            print(f"✅ Good! '{guess}' is in the word.")
        else:
            guessed.append(guess)
            tries -= 1
            print(f"❌ Wrong! '{guess}' is not in the word.")

    print(f"\n❌ Game Over! The word was: {word}")
    print(f"You guessed: {', '.join(sorted(guessed))}")
