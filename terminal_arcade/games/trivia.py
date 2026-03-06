import json
import random
from utils import title


def play():

    title("TRIVIA")

    try:
        with open("questions.json") as f:
            questions = json.load(f)
    except FileNotFoundError:
        print("❌ Error: questions.json file not found!")
        return
    except json.JSONDecodeError:
        print("❌ Error: questions.json is not valid JSON!")
        return

    if not questions:
        print("❌ Error: No questions found in questions.json")
        return

    random.shuffle(questions)

    score = 0
    total_questions = min(5, len(questions))

    print(f"\n❓ Answer {total_questions} trivia questions!")
    print("   Get them right to score points.\n")

    for q_num, q in enumerate(questions[:total_questions], 1):

        print(f"\n{'='*50}")
        print(f"Question {q_num}/{total_questions}")
        print(f"{'='*50}")
        print(f"\n{q['q']}\n")

        for i, opt in enumerate(q["options"], 1):
            print(f"   {i}) {opt}")

        while True:
            try:
                ans = int(input("\nYour answer (1-4): ")) - 1
                if ans < 0 or ans >= len(q["options"]):
                    print(
                        f"❌ Please enter a number between 1 and {len(q['options'])}.")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid number.")

        if ans == q["correct"]:
            print("✅ Correct!")
            score += 1
        else:
            correct_answer = q["options"][q["correct"]]
            print(f"❌ Wrong! The correct answer was: {correct_answer}")

    print(f"\n{'='*50}")
    print(f"Game Over!")
    print(f"Final Score: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    print(f"{'='*50}")
