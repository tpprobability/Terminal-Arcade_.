import random
import os
import time
from utils import title
from collections import deque


class AdvancedSnakeGame:
    def __init__(self, difficulty="normal", barriers=False):
        self.width = 40
        self.height = 20
        self.snake = deque([(self.width // 2, self.height // 2)])
        self.barriers = set()
        self.food = set()  # Initialize empty first
        self.direction = (1, 0)  # (x, y) velocity
        self.next_direction = (1, 0)
        self.prev_direction = (1, 0)
        self.score = 0
        self.high_score = 0
        self.game_over = False
        self.difficulty = difficulty
        self.barriers_enabled = barriers
        self.speed_multiplier = self.get_speed_multiplier()
        # Now spawn initial food
        self.food.add(self.spawn_food())

    def get_speed_multiplier(self):
        speeds = {"slow": 0.5, "normal": 1.0, "fast": 1.5, "expert": 2.0}
        return speeds.get(self.difficulty, 1.0)

    def spawn_food(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.snake and (x, y) not in self.barriers and (x, y) not in self.food:
                return (x, y)

    def spawn_barrier(self):
        if not self.barriers_enabled or len(self.barriers) > 5:
            return
        while True:
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
            if (x, y) not in self.snake and (x, y) not in self.food and (x, y) not in self.barriers:
                self.barriers.add((x, y))
                break

    def update(self):
        self.prev_direction = self.direction
        self.direction = self.next_direction

        # Prevent reversing into self
        if (self.direction[0] * -1, self.direction[1] * -1) == self.prev_direction:
            self.direction = self.prev_direction

        head_x, head_y = self.snake[0]
        new_x = head_x + self.direction[0]
        new_y = head_y + self.direction[1]

        # Wall collision
        if new_x < 0 or new_x >= self.width or new_y < 0 or new_y >= self.height:
            self.game_over = True
            return

        new_head = (new_x, new_y)

        # Self collision
        if new_head in self.snake:
            self.game_over = True
            return

        # Barrier collision
        if new_head in self.barriers:
            self.game_over = True
            return

        self.snake.appendleft(new_head)

        if new_head in self.food:
            self.score += 10
            self.food.discard(new_head)
            self.food.add(self.spawn_food())

            # Spawn barrier every 50 points
            if self.score % 50 == 0:
                self.spawn_barrier()

            # Increase difficulty
            if self.difficulty == "expert" and self.score % 100 == 0:
                self.width = max(20, self.width - 1)
        else:
            self.snake.pop()

    def get_direction_char(self, current_dir, next_dir=None):
        """Get display character based on direction"""
        chars = {
            ((1, 0), (1, 0)): "→",   # Moving right
            ((-1, 0), (-1, 0)): "←",  # Moving left
            ((0, -1), (0, -1)): "↑",  # Moving up
            ((0, 1), (0, 1)): "↓",    # Moving down
            ((1, 0), (0, -1)): "↗",   # Right-Up corner
            ((1, 0), (0, 1)): "↘",    # Right-Down corner
            ((-1, 0), (0, -1)): "↖",  # Left-Up corner
            ((-1, 0), (0, 1)): "↙",   # Left-Down corner
        }

        if next_dir is None:
            next_dir = current_dir

        return chars.get((current_dir, next_dir), "●")

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "="*50)
        print("          🐍 ADVANCED SNAKE GAME 🐍")
        print("="*50)
        print(
            f"Difficulty: {self.difficulty.upper()} | Score: {self.score} | Best: {self.high_score}\n")

        # Draw game board
        print("┌" + "─"*40 + "┐")

        snake_list = list(self.snake)
        for y in range(self.height):
            print("│", end="")
            for x in range(self.width):
                if (x, y) == self.snake[0]:
                    # Head with direction
                    if len(snake_list) > 1:
                        next_pos = snake_list[1]
                        dir_to_next = (
                            self.snake[0][0] - next_pos[0], self.snake[0][1] - next_pos[1])
                        print(self.get_direction_char(
                            self.direction, dir_to_next), end="")
                    else:
                        print(self.get_direction_char(self.direction), end="")
                elif (x, y) in self.snake:
                    print("●", end="")
                elif (x, y) in self.food:
                    print("🍎", end="")
                elif (x, y) in self.barriers:
                    print("■", end="")
                else:
                    print(" ", end="")
            print("│")

        print("└" + "─"*40 + "┘")
        print("\n📊 Stats:")
        print(
            f"   Length: {len(self.snake)} | Speed: {self.speed_multiplier}x | Barriers: {len(self.barriers)}")
        print("\n⌨️  Controls: (w)up, (s)down, (a)left, (d)right | (q)uit")
        print("="*50)


def play():
    title("ADVANCED SNAKE")

    print("\nSelect difficulty level:\n")
    print("1. Slow (0.5x speed)")
    print("2. Normal (1.0x speed)")
    print("3. Fast (1.5x speed)")
    print("4. Expert (2.0x speed, growing map!)")
    print("5. Back to menu\n")

    while True:
        choice = input("Choose difficulty (1-5): ").strip()
        if choice in ['1', '2', '3', '4', '5']:
            break
        print("❌ Invalid choice! Please enter 1-5.\n")

    if choice == '5':
        return

    difficulty_map = {'1': 'slow', '2': 'normal', '3': 'fast', '4': 'expert'}
    difficulty = difficulty_map[choice]

    # Ask about barriers
    barriers = False
    if difficulty != 'expert':
        print("\nEnable barriers? (y/n): ", end="")
        barriers = input().lower().strip() == 'y'

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n🐍 Starting game...\n")
    print("Game starting in 3 seconds...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)

    game = AdvancedSnakeGame(difficulty, barriers)

    print("\n🎮 Welcome to Advanced SNAKE!")
    print("Eat the food (🍎) to grow and score points!")
    if barriers:
        print("Avoid barriers (■) or you'll crash!")
    if difficulty == 'expert':
        print("⚠️  Expert mode: Map shrinks as you progress!")
    print("\nPress any key to start...\n")
    input()

    try:
        while not game.game_over:
            game.draw()

            key = input("\n➤ Your move (w/a/s/d or q): ").lower().strip()

            if key == 'q':
                print("\n👋 Thanks for playing!\n")
                return
            elif key == 'w' and game.direction != (0, 1):
                game.next_direction = (0, -1)
            elif key == 's' and game.direction != (0, -1):
                game.next_direction = (0, 1)
            elif key == 'a' and game.direction != (1, 0):
                game.next_direction = (-1, 0)
            elif key == 'd' and game.direction != (-1, 0):
                game.next_direction = (1, 0)

            game.update()

        game.draw()
        print(f"\n💀 GAME OVER!")
        print(f"{'='*50}")
        print(f"🏁 Final Score: {game.score}")
        print(f"📏 Snake Length: {len(game.snake)}")
        print(f"🎮 Difficulty: {game.difficulty.upper()}")
        print(
            f"⚡ Barriers: {'Enabled' if game.barriers_enabled else 'Disabled'}")
        print(f"{'='*50}\n")

    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!\n")
