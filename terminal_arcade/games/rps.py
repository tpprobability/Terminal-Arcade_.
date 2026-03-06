import random
from utils import title


def play():

    title("ROCK PAPER SCISSORS")

    choices = ["rock", "paper", "scissors"]
    player_wins = 0
    cpu_wins = 0

    print("\n🎮 Play Rock, Paper, Scissors!")
    print("Type 'quit' to exit.\n")

    while True:

        print(f"Score - You: {player_wins} | CPU: {cpu_wins}")

        while True:
            player = input(
                "\nYour choice (rock/paper/scissors): ").lower().strip()

            if player == "quit":
                print(f"\n👋 Thanks for playing!")
                print(f"Final Score - You: {player_wins} | CPU: {cpu_wins}")
                return

            if player not in choices:
                print("❌ Please choose rock, paper, scissors, or quit.")
                continue
            break

        cpu = random.choice(choices)

        print(f"\nYou chose:  {player}")
        print(f"CPU chose:  {cpu}")

        if player == cpu:
            print("🤝 It's a Tie!")

        elif (
            (player == "rock" and cpu == "scissors") or
            (player == "paper" and cpu == "rock") or
            (player == "scissors" and cpu == "paper")
        ):
            print("✅ You win this round!")
            player_wins += 1

        else:
            print("❌ CPU wins this round!")
            cpu_wins += 1

        input("\nPress Enter to continue...")
