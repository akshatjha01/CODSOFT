import random

board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("--+---+--")

def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for win in wins:
        if all(board[i] == player for i in win):
            return True
    return False

def ai_move():
    empty = [i for i in range(9) if board[i] == " "]
    return random.choice(empty)

print("=== AI TIC TAC TOE ===")
print("You = X | Computer = O")

while True:
    print_board()

    move = int(input("Enter position (1-9): ")) - 1

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid Move!")
        continue

    board[move] = "X"

    if check_winner("X"):
        print_board()
        print("You Win!")
        break

    if " " not in board:
        print_board()
        print("Draw!")
        break

    computer = ai_move()
    board[computer] = "O"

    print(f"\nComputer chose position {computer+1}\n")

    if check_winner("O"):
        print_board()
        print("Computer Wins!")
        break

    if " " not in board:
        print_board()
        print("Draw!")
        break