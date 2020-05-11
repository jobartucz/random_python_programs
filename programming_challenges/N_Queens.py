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

def nQueen(n):
    explanation = ''' from WikiPedia
    If the remainder from dividing n by 6 is not 2 or 3 then the list is simply all even numbers followed by all odd numbers not greater than n.
    Otherwise, write separate lists of even and odd numbers (2, 4, 6, 8 – 1, 3, 5, 7).
    If the remainder is 2, swap 1 and 3 in odd list and move 5 to the end (3, 1, 7, 5).
    If the remainder is 3, move 2 to the end of even list and 1,3 to the end of odd list (4, 6, 8, 2 – 5, 7, 1, 3).
    Append odd list to the even list and place queens in the rows given by these numbers, from left to right (a2, b4, c6, d8, e3, f1, g7, h5).'''

    evens = []
    odds = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            evens.append(i)
    for i in range(1, n + 1):
        if i % 2 == 1:
            odds.append(i)

    remainder = n % 6

    if remainder == 2:
        odds[0] = 3
        odds[1] = 1
        odds.pop(2)
        odds.append(5)

    if remainder == 3:
        evens.pop(0)
        evens.append(2)
        odds.pop(0)
        odds.append(1)
        odds.pop(0)
        odds.append(3)

    board = []
    for i in evens:
        board.append(i - 1)
    for i in odds:
        board.append(i - 1)
    return board

print(nQueen(20))