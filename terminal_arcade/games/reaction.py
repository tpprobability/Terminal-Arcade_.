import random
import time
from utils import title, wait


def play():

    title("REACTION TEST")

    print("\n⏱️  Test your reaction time!")
    print("   Wait for 'GO!' then press Enter as fast as you can.")
    print("   Ready? Starting in 3...\n")

    for countdown in range(3, 0, -1):
        print(f"   {countdown}...", flush=True)
        time.sleep(1)

    wait_time = random.uniform(2, 5)
    print("   Getting ready...", flush=True)

    wait(wait_time)

    print("\n🎯 GO! Press Enter NOW!")

    start = time.time()
    input()

    reaction = time.time() - start

    print(f"\n⏱️  Your reaction time: {reaction:.3f} seconds")
    if reaction < 0.3:
        print("🏆 Incredible! You have amazing reflexes!")
    elif reaction < 0.5:
        print("⭐ Excellent reaction time!")
    elif reaction < 0.8:
        print("✅ Good reaction time!")
    else:
        print("⏰ Keep practicing to improve!")
