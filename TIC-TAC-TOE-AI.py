import random

def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(*row)

def is_empty(board, row, col):
    return board[row][col] == ' '

def is_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def evaluate(board):
    if check_win(board, 'O'):
        return 1
    elif check_win(board, 'X'):
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score != 0:
        return score

    if is_full(board):
        return 0

    if is_maximizing:
        best_val = -float('inf')
        for i in range(3):
            for j in range(3):
                if is_empty(board, i, j):
                    board[i][j] = 'O'
                    value = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_val = max(best_val, value)
        return best_val
    else:
        best_val = float('inf')
        for i in range(3):
            for j in range(3):
                if is_empty(board, i, j):
                    board[i][j] = 'X'
                    value = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_val = min(best_val, value)
        return best_val

def find_best_move(board):
    best_val = -float('inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if is_empty(board, i, j):
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

def play_game():
    board = create_board()
    while True:
        print_board(board)

        # Player's move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if not is_empty(board, row, col):
            print("Invalid move!")
            continue
        board[row][col] = 'X'

        if check_win(board, 'X'):
            print_board(board)
            print("You win!")
            break

        if is_full(board):
            print_board(board)
            print("Tie!")
            break

        # AI's move
        row, col = find_best_move(board)
        board[row][col] = 'O'

        if check_win(board, 'O'):
            print_board(board)
            print("AI wins!")
            break

        if is_full(board):
            print_board(board)
            print("Tie!")
            break

play_game()
