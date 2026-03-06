import random
import json
from utils import title


def play():

    title("WORDLE")

    try:
        with open("words.json") as f:
            word_data = json.load(f)
        words = word_data.get("wordle", [])
        if not words:
            print("❌ Error: No wordle words found in words.json")
            return
    except FileNotFoundError:
        print("❌ Error: words.json file not found!")
        print("Please ensure words.json is in the terminal_arcade directory.")
        return
    except json.JSONDecodeError:
        print("❌ Error: words.json is not valid JSON!")
        return

    word = random.choice(words).lower()
    guesses = 0
    max_attempts = 6

    print(f"\n🎲 Guess the {len(word)}-letter word!")
    print("Hints:")
    print("  ✓ Correct letter in correct position")
    print("  ? Correct letter in wrong position")
    print("  _ Letter not in word")
    print(f"\nYou have {max_attempts} attempts.\n")

    for attempt in range(1, max_attempts + 1):

        while True:
            guess = input(
                f"Attempt {attempt}/{max_attempts} - Guess: ").lower().strip()
            if len(guess) != len(word):
                print(f"❌ Please enter a {len(word)}-letter word.")
                continue
            if not guess.isalpha():
                print("❌ Please enter only letters.")
                continue
            break

        if guess == word:
            print(f"\n✅ Correct! The word was: {word}")
            print(f"You found it in {attempt} attempt(s)!")
            return

        hint = ""

        for i in range(len(word)):
            if guess[i] == word[i]:
                hint += f"✓{guess[i]}"
            elif guess[i] in word:
                hint += f"?{guess[i]}"
            else:
                hint += f"_{guess[i]}"
            hint += " "

        print(f"Hint: {hint.strip()}")
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"Remaining attempts: {remaining}\n")

    print(f"\n❌ Game Over! The word was: {word}")
