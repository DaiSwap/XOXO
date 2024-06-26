import math
import copy

X: str = "X"
O: str = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    return O if x_count > o_count else X


def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    if action not in actions(board):
        raise Exception("Not valid action")
    row, col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
    return board_copy


def checkRow(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False

def checkCol(board, player):
    for col in range(len(board[0])):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False

def checkFirstDig(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == player:
                count += 1
    return count == 3

def checkSecondDig(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count += 1
    return count == 3


def winner(board):
    if checkRow(board, X) or checkCol(board, X) or checkFirstDig(board, X) or checkSecondDig(board, X):
        return X
    if checkRow(board, O) or checkCol(board, O) or checkFirstDig(board, O) or checkSecondDig(board, O):
        return O
    return None


def terminal(board):
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    win = winner(board)
    if win == X:
        return 1
    if win == O:
        return -1
    return 0

def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    if terminal(board):
        return None

    if board == initial_state():
        return (1, 1)

    current_player = player(board)
    possible_actions = actions(board)

    if current_player == X:
        best_value = -math.inf
        best_action = None
        for action in possible_actions:
            action_value = min_value(result(board, action))
            if action_value > best_value:
                best_value = action_value
                best_action = action
        return best_action
    else:
        best_value = math.inf
        best_action = None
        for action in possible_actions:
            action_value = max_value(result(board, action))
            if action_value < best_value:
                best_value = action_value
                best_action = action
        return best_action
