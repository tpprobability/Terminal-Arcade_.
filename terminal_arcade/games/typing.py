import time
import random
from utils import title

sentences = [
    "python is a powerful programming language",
    "coding every day improves your skills",
    "practice makes perfect in programming",
    "terminal games are fun to build"
]


def play():

    title("TYPING SPEED TEST")

    sentence = random.choice(sentences)

    print("\n⌨️  Typing Speed Test")
    print("="*50)
    print("\nType this sentence as quickly and accurately as you can:\n")
    print(f"\n  '{sentence}'\n")
    print("="*50)

    input("\n👆 Press Enter when ready to start...")

    print("\n🟢 GO! Start typing now:\n")

    start = time.time()

    typed = input()

    end = time.time()
    elapsed_time = end - start

    if typed == sentence:
        word_count = len(sentence.split())
        speed = word_count / (elapsed_time / 60) if elapsed_time > 0 else 0
        accuracy = 100
        print(f"\n{'='*50}")
        print("✅ Perfect! Exact match!")
        print(f"Time: {elapsed_time:.2f} seconds")
        print(f"Words per minute (WPM): {int(speed)}")
        print(f"Accuracy: {accuracy}%")
        print(f"{'='*50}")
    else:
        typed_words = len(typed.split()) if typed else 0
        expected_words = len(sentence.split())
        correct_chars = sum(1 for i, c in enumerate(
            typed) if i < len(sentence) and c == sentence[i])
        total_chars = len(sentence)
        accuracy = (correct_chars / total_chars *
                    100) if total_chars > 0 else 0

        print(f"\n{'='*50}")
        print("❌ Text didn't match exactly.")
        print(f"\nExpected: '{sentence}'")
        print(f"You typed: '{typed}'")
        print(f"\nTime: {elapsed_time:.2f} seconds")
        print(f"Accuracy: {accuracy:.1f}%")
        print(f"Words typed: {typed_words}/{expected_words}")
        print(f"{'='*50}")
