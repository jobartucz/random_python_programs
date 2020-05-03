problem = '''This is a classic needing (almost) no further introduction.

Given a N x N chess board, place N queens on it so none can attack another: I.e. no other queens can be found horizontally, vertically or diagonally to the current.

On the board below, no further queens can be positioned.

+-+-+
|Q| |
+-+-+
| | |
+-+-+


In this example a queen can be located in position a or position b - but not in both, thereby making (0,0) an invalid first position:

+-+-+-+
|Q| | |
+-+-+-+
| | |a|
+-+-+-+
| |b| |
+-+-+-+


Return value must by an array of N x-positions. That is, the y position is given by the index.

Only one solution per N is expected. If no solution can be found, return an empty array. That is, for a 1 x 1 board, the output is [0].

Input is a value positive number (N>0) and can be quite high, so try to make your solution efficient.

Have fun :)
'''


def checkspot(y, x, board):

    # we can only check rows that have gone before
    for i in range(y):
        if board[i] == x:
            # we've already used this x
            return False
        
        # slope +1
        if board[i] + i == x + y:
            return False

        # slope -1
        if board[i] - i == x - y:
            return False

    return True

def nQueen_greedy_doesntwork(n):

    board = [-1 for x in range(n)]

    board[0] = 0
    # for every row
    for i in range(1, n):
        # for every spot
        for j in range(1, n):
            # check to see if we can place it
            if checkspot(i, j, board):
                board[i] = j
                break

        if board[i] == j:
            continue
        if board[i] == -1:
            # no placement
            return []

    return board

def placenext(board, level):

    if level == len(board):
        return board

    for x in range(len(board)):
        if checkspot(level, x, board) == True:
            board[level] = x
            tempboard = placenext(board, level + 1)
            if len(tempboard) > 0:
                return tempboard
        
    return []


def nQueen_brute(n):
    board = [-1 for x in range(n)]

    return(placenext(board, 0))

print(nQueen(8))