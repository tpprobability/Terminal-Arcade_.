import random
from utils import title


def play():

    title("DICE GAME")

    score = 0
    print("\n🎲 Roll the dice without getting a 1!")
    print("Rolling 1 resets your score to 0.\n")

    while True:

        while True:
            roll = input(
                f"Your score: {score}\nRoll dice? (y/n): ").lower().strip()
            if roll in ["y", "n"]:
                break
            print("❌ Please enter 'y' or 'n'.")

        if roll != "y":
            print(f"\n✅ Game ended. Final score: {score}")
            break

        dice = random.randint(1, 6)

        print(f"\n🎲 You rolled: {dice}")

        if dice == 1:
            print("\n❌ Oh no! You rolled a 1. Your score resets to 0!")
            score = 0
        else:
            score += dice
            print(f"✅ +{dice} points!")

        print(f"Current score: {score}\n")
