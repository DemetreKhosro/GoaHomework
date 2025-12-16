import random

# Display the board in terminal
def display_board(board):
    for r in range(3):
        row = ""
        for c in range(3):
            if c > 0:
                row += " | "
            row += board[r][c]
        print(" " + row + " ")
        if r < 2:
            # row separator
            print("-----------")

# Check if the player has won
def check_winner(board, player):
    # check rows
    for r in range(3):
        win = True
        for c in range(3):
            if board[r][c] != player:
                win = False
        if win:
            return True
    # check columns
    for c in range(3):
        win = True
        for r in range(3):
            if board[r][c] != player:
                win = False
        if win:
            return True
    # check main diagonal
    win = True
    for i in range(3):
        if board[i][i] != player:
            win = False
    if win:
        return True
    # check anti-diagonal
    win = True
    for i in range(3):
        if board[i][2-i] != player:
            win = False
    if win:
        return True
    return False

# Check if the board is full
def board_full(board):
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                return False
    return True

# Player move input
def player_move(board, player):
    while True:
        move = input(player + "'s turn (1-9): ")
        # check if input is a number
        if not move.isdigit():
            continue
        move = int(move)
        # check range
        if move < 1 or move > 9:
            continue
        r = (move - 1) // 3
        c = (move - 1) % 3
        # check if cell empty
        if board[r][c] == " ":
            board[r][c] = player
            break

# Simple AI move (random)
def ai_move(board, player):
    empty = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                empty.append((r,c))
    index = random.randint(0, len(empty)-1)
    r, c = empty[index]
    board[r][c] = player

# Main game loop
def tic_tac_toe():
    print("Tic Tac Toe")
    mode = input("Mode: 1=2 players, 2=vs AI: ")
    # track scores
    scores = {"X": 0, "O": 0}

    while True:
        # create empty board
        board = []
        for i in range(3):
            board.append([" "]*3)
        current = "X"
        display_board(board)

        # play until win or tie
        while True:
            if mode == "2" and current == "O":
                # AI turn
                ai_move(board, current)
                print("AI moved:")
            else:
                # Player turn
                player_move(board, current)  
            display_board(board)

            # check win
            if check_winner(board, current):
                print(current + " wins!")
                scores[current] = scores[current] + 1
                break
            # check tie
            if board_full(board):
                print("Tie!")
                break

            # switch player
            if current == "X":
                current = "O"
            else:
                current = "X"

        # show scores
        print("Scores: X=" + str(scores["X"]) + ", O=" + str(scores["O"]))
        again = input("Play again? (y/n): ")
        if again != "y":
            break

tic_tac_toe()