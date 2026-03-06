import os
import time


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def title(text):
    print("="*50)
    print(text.center(50))
    print("="*50)


def wait(seconds):
    time.sleep(seconds)
