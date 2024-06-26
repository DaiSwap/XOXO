import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return O if x_count > o_count else X

def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    if action not in actions(board):
        raise Exception("Invalid action")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board

def check_winner(board, mark):
    return any(
        all(board[i][j] == mark for j in range(3)) for i in range(3)
    ) or any(
        all(board[i][j] == mark for i in range(3)) for j in range(3)
    ) or all(
        board[i][i] == mark for i in range(3)
    ) or all(
        board[i][2 - i] == mark for i in range(3)
    )

def winner(board):
    if check_winner(board, X):
        return X
    if check_winner(board, O):
        return O
    return None

def terminal(board):
    return winner(board) is not None or all(EMPTY not in row for row in board)

def utility(board):
    win = winner(board)
    if win == X:
        return 1
    if win == O:
        return -1
    return 0

def minimax_value(board, maximizing):
    if terminal(board):
        return utility(board)
    if maximizing:
        value = -math.inf
        for action in actions(board):
            value = max(value, minimax_value(result(board, action), False))
        return value
    else:
        value = math.inf
        for action in actions(board):
            value = min(value, minimax_value(result(board, action), True))
        return value

def minimax(board):
    if terminal(board):
        return None
    current_player = player(board)
    possible_actions = actions(board)
    best_action = None
    if current_player == X:
        best_value = -math.inf
        for action in possible_actions:
            action_value = minimax_value(result(board, action), False)
            if action_value > best_value:
                best_value = action_value
                best_action = action
    else:
        best_value = math.inf
        for action in possible_actions:
            action_value = minimax_value(result(board, action), True)
            if action_value < best_value:
                best_value = action_value
                best_action = action
    return best_action
