import math

# Function to print the current board state
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # Top row
        [board[1][0], board[1][1], board[1][2]],  # Middle row
        [board[2][0], board[2][1], board[2][2]],  # Bottom row
        [board[0][0], board[1][0], board[2][0]],  # Left column
        [board[0][1], board[1][1], board[2][1]],  # Middle column
        [board[0][2], board[1][2], board[2][2]],  # Right column
        [board[0][0], board[1][1], board[2][2]],  # Diagonal from top-left
        [board[2][0], board[1][1], board[0][2]],  # Diagonal from bottom-left
    ]
    return [player, player, player] in win_conditions

# Function to get a list of all available moves (empty spots on the board)
def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves

# Function to make a move on the board
def make_move(board, move, player):
    board[move[0]][move[1]] = player

# Function implementing the Alpha-Beta Pruning algorithm
def alpha_beta_pruning(board, depth, alpha, beta, is_maximizing):
    if check_winner(board, "O"):  # If AI wins
        return 1
    elif check_winner(board, "X"):  # If player wins
        return -1
    elif not get_available_moves(board):  # If it's a tie
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            make_move(board, move, "O")
            eval = alpha_beta_pruning(board, depth + 1, alpha, beta, False)
            make_move(board, move, " ")
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:  # Beta cutoff
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
            if beta <= alpha:  # Alpha cutoff
                break
        return min_eval

# Function to determine the best move for the AI
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

# Main function to run the Tic-Tac-Toe game
def main():
    # Initialize an empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        if current_player == "X":
            # Human player's move
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
            if (row, col) not in get_available_moves(board):
                print("Invalid move. Try again.")
                continue
            make_move(board, (row, col), current_player)
        else:
            # AI's move
            print("AI is making a move...")
            move = get_best_move(board)
            make_move(board, move, current_player)

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if not get_available_moves(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    main()
