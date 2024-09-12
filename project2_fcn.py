'''
DO NOT MODIFY THIS FILE!

This file contains the function that you will USE in project2.py.

'''


def can_play(board, dice1, dice2):
    '''
    can_play(board, dice1, dice2) is a function that takes in a list of integers
    representing the board, and two integers representing the values of two dice.
    The function returns True if the two dice can be used to move a piece on the
    board, and False otherwise.

    Arguments:
    board: a list of integers representing the board. The board will contain
    at 9 integers, and each integer will be between 0 and 9, inclusive.
    dice1: an integer representing the value of the first die. The value will be
    between 1 and 6, inclusive.
    dice2: an integer representing the value of the second die. The value will be
    between 1 and 6, inclusive.

    Returns:
    True if the two dice can be used to move a piece on the board, 
    and False otherwise.
    '''
    total = dice1 + dice2
    if total in board:
        return True
    # Double numbers
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i] + board[j] == total:
                return True
    # Triple numbers
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            for k in range(j+1, len(board)):
                if board[i] + board[j] + board[k] == total:
                    return True
    # 4 numbers
    solns = [[1, 2, 3, 4],
             [1, 2, 3, 5],
             [1, 2, 3, 6],
             [1, 2, 4, 5]]
    for soln in solns:
        if sum(soln) == total:
            c = 0
            for n in soln:
                if n in board:
                    c += 1
            if c == 4:
                print(soln)
                return True
    return False