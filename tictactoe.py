import math

board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

def is_draw():
    return " " not in board

def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score

def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move

print("=== AI TIC TAC TOE ===")
print("You = X")
print("Computer = O")

while True:

    print_board()

    try:
        move = int(input("Enter position (1-9): ")) - 1

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move!")
            continue

    except:
        print("Enter a valid number!")
        continue

    board[move] = "X"

    if check_winner("X"):
        print_board()
        print("🎉 You Win!")
        break

    if is_draw():
        print_board()
        print("🤝 Draw!")
        break

    computer = ai_move()
    board[computer] = "O"

    print(f"Computer chose position {computer + 1}")

    if check_winner("O"):
        print_board()
        print("🤖 AI Wins!")
        break

    if is_draw():
        print_board()
        print("🤝 Draw!")
        break