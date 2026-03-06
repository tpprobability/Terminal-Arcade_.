import random
import time
from utils import title


def play():

    title("MEMORY GAME")

    sequence = []
    round_num = 1

    print("\n🧠 Remember the number sequence!")
    print("The sequence gets longer each round.\n")

    while True:

        sequence.append(random.randint(1, 9))

        print(f"\n🔄 Round {round_num}")
        print(f"Sequence has {len(sequence)} number(s)")
        print("\nSequence: ", end="")

        for n in sequence:
            print(n, end=" ", flush=True)
            time.sleep(0.7)

        print("\n\n" + "-"*40)

        while True:
            try:
                user_input = input(
                    "Enter the sequence (space-separated): ").strip()
                if not user_input:
                    print("❌ Please enter at least one number.")
                    continue
                user = [int(x) for x in user_input.split()]
                break
            except ValueError:
                print("❌ Please enter valid numbers separated by spaces.")

        if user != sequence:
            print(f"\n❌ Wrong! You entered: {user}")
            print(f"The correct sequence was: {sequence}")
            print(f"\nYou made it to Round {round_num}!")
            break

        print(f"✅ Correct! Sequence remembered!")
        round_num += 1
