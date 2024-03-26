"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num = 0
    for row in board:
        num += row.count(X)
        num += row.count(O)
    if num % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    acts = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                acts.add((i, j))
    return acts



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    nboard = copy.deepcopy(board)
    i, j = action
    nboard[i][j] = player(board)
    return nboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O

    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X

    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O

    nboard = zip(*board)

    for row in nboard:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O

    return None




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    for row in board:
        if row.count(EMPTY) != 0:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        return Max(board)
    if player(board) == O:
        return Min(board)

def Max(board):
    v = -10
    for action in actions(board): 
        vn = min_value(result(board, action)) 
        if vn > v:
            v = vn
            act = action
    return act

def Min(board):
    v = 10
    for action in actions(board):
        vn = max_value(result(board, action))
        if vn < v:
            v = vn
            act = action
    return act

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -10
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = 10
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

if  __name__ == "__main__":
    s1 = [  [X, EMPTY, EMPTY],
            [X, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    print(minimax(s1))

