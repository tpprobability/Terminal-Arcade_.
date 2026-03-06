import random
from utils import title


def play():

    title("NUMBER GUESS")

    num = random.randint(1, 100)
    attempts = 7

    print("\n🔢 I'm thinking of a number between 1-100.")
    print(f"You have {attempts} guesses. Good luck!\n")

    for guess_count in range(1, attempts + 1):

        while True:
            try:
                guess = int(input(f"Guess {guess_count}/{attempts}: "))
                if guess < 1 or guess > 100:
                    print("❌ Please guess a number between 1 and 100.")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid number.")

        if guess == num:
            print(f"\n✅ Correct! The number was {num}!")
            print(f"You guessed it in {guess_count} attempt(s)!")
            return

        elif guess < num:
            remaining = attempts - guess_count
            print(f"📈 Higher! ({remaining} guess(es) remaining)")

        else:
            remaining = attempts - guess_count
            print(f"📉 Lower! ({remaining} guess(es) remaining)")

    print(f"\n❌ Game Over! The number was {num}")
