import random

board = {'t1':' ','t2':' ','t3':' ','m1':' ','m2':' ','m3':' ','b1':' ','b2':' ','b3':' '}

def printboard():
    print ('')
    print (board['t1'] + '|' + board['t2'] + '|' + board['t3'])
    print ('-|-|-')
    print (board['m1'] + '|' + board['m2'] + '|' + board['m3'])
    print ('-|-|-')
    print (board['b1'] + '|' + board['b2'] + '|' + board['b3'])
    print ('')

def checkinput(val):
    if (val not in ['t1', 't2', 't3', 'm1', 'm2', 'm3', 'b1', 'b2', 'b3']):
        print ("Invalid command")
        return False
    if (board[val] != ' '):
        print ("That space is taken")
        return False
    return True

def checkwinner(player):
    # check possibilities for top left
    if (board['t1'] == player):
        if (board['t2'] == player and board['t3'] == player):
            return True
        if (board['m2'] == player and board['b3'] == player):
            return True
        if (board['m1'] == player and board['b1'] == player):
            return True
    # check remaining possibilities for top 2
    if (board['t2'] == player):
        if (board['m2'] == player and board['b2'] == player):
            return True
    # check remaining possibilities for top right
    if (board['t3'] == player):
        if (board['m3'] == player and board['b3'] == player):
            return True
        if (board['m2'] == player and board['b1'] == player):
            return True
    # check remaining possibilities for middle
    if (board['m1'] == player):
        if (board['m2'] == player and board['m3'] == player):
            return True
    # check remaining possibilities for bottom
    if (board['b1'] == player):
        if (board['b2'] == player and board['b3'] == player):
            return True

    if (' ' not in board.values()):
        return 'cat'
    
    return False

# random, not very smart, but win the game if close
def computermove(player):
    movespossible = []
    for move in board.keys():
        if (board[move] == ' '):
            movespossible.append(move)

    if (player == 'X'):
        opponent = 'Y'
    else:
        opponent = 'X'

    if ('t1' in movespossible):
        if (board['t2'] == player and board['t3'] == player) or (board['t2'] == opponent and board['t3'] == opponent):
            return 't1'
        if (board['m2'] == player and board['b3'] == player) or (board['m2'] == opponent and board['b3'] == opponent):
            return 't1'
        if (board['m1'] == player and board['b1'] == player) or (board['m1'] == opponent and board['b1'] == opponent):
            return 't1'
    if ('t2' in movespossible):
        if (board['t1'] == player and board['t3'] == player) or (board['t1'] == opponent and board['t3'] == opponent):
            return 't2'
        if (board['m2'] == player and board['b2'] == player) or (board['m2'] == opponent and board['b2'] == opponent):
            return 't2'
    if ('t3' in movespossible):
        if (board['t1'] == player and board['t2'] == player) or (board['t1'] == opponent and board['t2'] == opponent):
            return 't3'
        if (board['m2'] == player and board['b1'] == player) or (board['m2'] == opponent and board['b1'] == opponent):
            return 't3'
        if (board['m3'] == player and board['b3'] == player) or (board['m3'] == opponent and board['b3'] == opponent):
            return 't3'
    if ('m1' in movespossible):
        if (board['m2'] == player and board['m3'] == player) or (board['m2'] == opponent and board['m3'] == opponent):
            return 'm1'
        if (board['t1'] == player and board['b1'] == player) or (board['t1'] == opponent and board['b1'] == opponent):
            return 'm1'
    if ('m2' in movespossible):
        if (board['t1'] == player and board['b3'] == player) or (board['t1'] == opponent and board['b3'] == opponent):
            return 'm2'
        if (board['m1'] == player and board['m3'] == player) or (board['m2'] == opponent and board['m3'] == opponent):
            return 'm2'
        if (board['t2'] == player and board['b2'] == player) or (board['t2'] == opponent and board['b2'] == opponent):
            return 'm2'
        if (board['t3'] == player and board['b1'] == player) or (board['t3'] == opponent and board['b1'] == opponent):
            return 'm2'
    if ('m3' in movespossible):
        if (board['t3'] == player and board['b3'] == player) or (board['t3'] == opponent and board['b3'] == opponent):
            return 'm3'
        if (board['m1'] == player and board['m2'] == player) or (board['m1'] == opponent and board['m2'] == opponent):
            return 'm3'
    if ('b1' in movespossible):
        if (board['t1'] == player and board['m1'] == player) or (board['t1'] == opponent and board['m1'] == opponent):
            return 'b1'
        if (board['m2'] == player and board['t3'] == player) or (board['m2'] == opponent and board['t3'] == opponent):
            return 'b1'
        if (board['b2'] == player and board['b3'] == player) or (board['b2'] == opponent and board['b3'] == opponent):
            return 'b1'
    if ('b2' in movespossible):
        if (board['t2'] == player and board['m2'] == player) or (board['t2'] == opponent and board['m2'] == opponent):
            return 'b2'
        if (board['b1'] == player and board['b3'] == player) or (board['b1'] == opponent and board['b3'] == opponent):
            return 'b2'
    if ('b3' in movespossible):
        if (board['t1'] == player and board['m2'] == player) or (board['t1'] == opponent and board['m2'] == opponent):
            return 'b3'
        if (board['b1'] == player and board['b2'] == player) or (board['b1'] == opponent and board['b2'] == opponent):
            return 'b3'
        if (board['t3'] == player and board['m3'] == player) or (board['t3'] == opponent and board['m3'] == opponent):
            return 'b3'

    return random.choice(movespossible)


print ("Welcome to tic tac toe! This is the current board:")
printboard()

print ("To place a marker, use:\nt1, t2, or t3 for the top row\nm1, m2, or m3 for the middle row and\nb1, b2, or b3 for the bottom row")

player = ''
while player not in ['X', 'Y']:
    player = input("\nWould you like to be X or Y? ").upper()

print ("\nX goes first!\n")

while True:
    
    if (player == 'X'):
        valid = False
        while valid == False:
            xmove = input ("Player X, where would you like your marker? ")
            valid = checkinput(xmove)
            
    else:
        xmove = computermove('X')
        print ("Computer chooses " + xmove)

    board[xmove] = 'X'
    printboard()
    
    if (checkwinner('X') == 'cat'):
        print ("Cat's game :/")
        break
    if (checkwinner('X') == True):
        print ("X is the winner!")
        break

    if (player == 'Y'):
        valid = False
        while valid == False:
            ymove = input ("Player Y, where would you like your marker? ")
            valid = checkinput(ymove)
    else:
        ymove = computermove('Y')
        print ("Computer chooses " + ymove)
        
    board[ymove] = 'Y'
    printboard()
    
    if (checkwinner('X') == 'cat'):
        print ("Cat's game :/")
        break
    if (checkwinner('Y') == True):
        print ("Y is the winner!")
        break