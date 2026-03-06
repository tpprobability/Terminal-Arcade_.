import random
from utils import title


def play():

    title("MINESWEEPER")

    size = 5
    mine = (random.randint(0, 4), random.randint(0, 4))
    safe_count = 0

    print(f"\n💣 There's 1 mine hidden in a 5x5 grid!")
    print(f"Coordinates are 0-4 for both row and column.\n")
    print("Grid positions:")
    print("  Col: 0 1 2 3 4")
    for i in range(5):
        print(f"Row {i}:     . . . . .")
    print()

    while True:

        while True:
            try:
                r = int(input("Enter row (0-4): "))
                if r < 0 or r > 4:
                    print("❌ Row must be between 0 and 4.")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid number.")

        while True:
            try:
                c = int(input("Enter column (0-4): "))
                if c < 0 or c > 4:
                    print("❌ Column must be between 0 and 4.")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid number.")

        if (r, c) == mine:
            print(f"\n💥 BOOM! You hit a mine at ({r}, {c})!")
            print(f"You found {safe_count} safe spots before hitting it.")
            break
        else:
            safe_count += 1
            print(f"✅ Safe! ({r}, {c}) is clear.")
            print(f"Safe spots found: {safe_count}\n")
