import random
from utils import title


def play():

    title("MASTERMIND")

    code = [random.randint(1, 6) for _ in range(4)]
    attempts = 0

    print("\n🔐 Crack the 4-digit code!")
    print("Each digit is between 1-6.")
    print("You have 10 attempts.\n")

    for attempt in range(1, 11):

        while True:
            try:
                guess_input = input(
                    f"Attempt {attempt}/10 - Enter 4 numbers (1-6): ").split()
                if len(guess_input) != 4:
                    print("❌ Please enter exactly 4 numbers.")
                    continue
                guess = [int(x) for x in guess_input]
                if any(x < 1 or x > 6 for x in guess):
                    print("❌ All numbers must be between 1 and 6.")
                    continue
                break
            except ValueError:
                print("❌ Please enter valid numbers only.")

        if guess == code:
            print(f"\n✅ You cracked the code! {guess}")
            print(f"You completed it in {attempt} attempts!")
            return

        correct = sum(1 for i in range(4) if guess[i] == code[i])

        print(f"✓ {correct} number(s) in correct position(s)")
        print()

    print(f"\n❌ Game Over! The code was: {code}")
