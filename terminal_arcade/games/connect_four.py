from utils import title


def play():

    title("CONNECT FOUR")

    board = [[" "]*7 for _ in range(6)]
    player = "X"

    def print_board():
        print("\n  0 1 2 3 4 5 6")
        for i, row in enumerate(board):
            print(f"{i} {'|'.join(row)}")
        print()

    print("\n📍 Connect four in a row to win!")
    print("Player X (You) vs Player O (Opponent)\n")

    while True:

        print_board()

        while True:
            try:
                col = int(input(f"Player {player}, enter column (0-6): "))
                if col < 0 or col > 6:
                    print("❌ Column must be between 0 and 6.")
                    continue
                if board[0][col] != " ":
                    print("❌ That column is full!")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid number between 0 and 6.")

        for r in range(5, -1, -1):
            if board[r][col] == " ":
                board[r][col] = player
                break

        player = "O" if player == "X" else "X"
