"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    x_count = 0
    o_count = 0
    for i in board:
        for j in i:
            if j == X:
                x_count += 1
            if j == O:
                o_count += 1
    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    final = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is None:
                final.add((i, j))

    return final


def result(board, action):
    player_move = player(board)

    new_board = deepcopy(board)
    i, j = action

    new_board[i][j] = player_move

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checking for horizontal
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]

    # Checking for Vertical
    for i in range(len(board)):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]

    # Checking for Diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] is not EMPTY:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for i in board:
        if EMPTY in i:
            return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    game_winner = winner(board)
    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def MinValCalc(board):
        optimal = ()
        if terminal(board) is True:
            return utility(board), optimal

        else:
            actions_lists = actions(board)
            tiniest = 10
            for action in actions_lists:
                resultant = result(board, action)
                minimum = MaxValCalc(resultant)[0]
                if minimum < tiniest:
                    tiniest = minimum
                    optimal = action
            return tiniest, optimal

    def MaxValCalc(board):
        optimal = ()
        if terminal(board) is True:
            return utility(board), optimal
        else:
            actions_lists = actions(board)
            biggest = -3
            for action in actions_lists:
                resultant = result(board, action)
                maximum = MinValCalc(resultant)[0]
                if maximum > biggest:
                    biggest = maximum
                    optimal = action
        return biggest, optimal

    player_turn = player(board)

    if player_turn == "X":
        return MaxValCalc(board)[1]
    elif player_turn == "O":
        return MinValCalc(board)[1]
