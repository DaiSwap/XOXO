import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves

def make_move(board, move, player):
    board[move[0]][move[1]] = player

def alpha_beta_pruning(board, depth, alpha, beta, is_maximizing):
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    elif not get_available_moves(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            make_move(board, move, "O")
            eval = alpha_beta_pruning(board, depth + 1, alpha, beta, False)
            make_move(board, move, " ")
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            make_move(board, move, "X")
            eval = alpha_beta_pruning(board, depth + 1, alpha, beta, True)
            make_move(board, move, " ")
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        make_move(board, move, "O")
        score = alpha_beta_pruning(board, 0, -math.inf, math.inf, False)
        make_move(board, move, " ")
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        if current_player == "X":
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
            if (row, col) not in get_available_moves(board):
                print("Invalid move. Try again.")
                continue
            make_move(board, (row, col), current_player)
        else:
            print("AI is making a move...")
            move = get_best_move(board)
            make_move(board, move, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if not get_available_moves(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
