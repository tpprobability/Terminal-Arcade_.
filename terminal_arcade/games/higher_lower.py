import random
from utils import title


def play():

    title("HIGHER LOWER")

    current = random.randint(1, 100)
    score = 0

    print("\n📊 I'm thinking of a number between 1-100.")
    print("Guess if the next number is HIGHER or LOWER!\n")

    while True:

        print(f"Current number: {current}")
        print(f"Current score: {score}")

        while True:
            guess = input(
                "\nNext number is (h)igher or (l)ower? ").lower().strip()
            if guess in ["h", "l"]:
                break
            print("❌ Please enter 'h' for higher or 'l' for lower.")

        next_num = random.randint(1, 100)

        print(f"\nNext number: {next_num}")

        if (guess == "h" and next_num > current) or (guess == "l" and next_num < current):
            score += 1
            print("✅ Correct!")
        else:
            print(f"❌ Wrong! You were incorrect.")
            break

        current = next_num

    print(f"\n🎉 Game Over! Final score: {score}")
