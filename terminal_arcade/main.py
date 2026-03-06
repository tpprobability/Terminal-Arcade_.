from utils import clear, pause, title
from games import *
from games import snake
from games import hangman
from games import rps
from games import number_guess
from games import trivia
from games import memory
from games import higher_lower
from games import blackjack
from games import connect_four
from games import minesweeper
from games import wordle
from games import mastermind
from games import dice_game
from games import reaction
from games import typing

games = {
    "1": ("Snake", snake.play),
    "2": ("Hangman", hangman.play),
    "3": ("Rock Paper Scissors", rps.play),
    "4": ("Number Guess", number_guess.play),
    "5": ("Trivia", trivia.play),
    "6": ("Memory Game", memory.play),
    "7": ("Higher Lower", higher_lower.play),
    "8": ("Blackjack", blackjack.play),
    "9": ("Connect Four", connect_four.play),
    "10": ("Minesweeper", minesweeper.play),
    "11": ("Wordle", wordle.play),
    "12": ("Mastermind", mastermind.play),
    "13": ("Dice Game", dice_game.play),
    "14": ("Reaction Test", reaction.play),
    "15": ("Typing Speed", typing.play)
}


def main():

    while True:

        clear()
        title("🎮 TERMINAL ARCADE")

        for key, game in games.items():
            print(f"{key}. {game[0]}")

        print("\n0. Exit\n")

        choice = input("Select a game: ").strip()

        if choice == "0":
            print("\nThanks for playing 👋")
            break

        if choice in games:
            clear()
            games[choice][1]()
        else:
            print("Invalid choice")

        pause()


if __name__ == "__main__":
    main()
