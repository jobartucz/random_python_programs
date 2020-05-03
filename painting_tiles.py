problem = '''You have a path of n tiles in your garden that you'd like to paint, and four different colors to do so.
'Thing is... You don't want any two adjacent tiles to be of the same color and you'd like that it'd cost you the minimum possible amount of money.
'Second thing is... due to differences in the texture and matter of each tile, the quantity of paint needed to cover each tile may differe a lot.
So, you are given n x 4 array, that represents the costs of painting each tile of the path with the four available colors and you need to find a way to get the minimal total cost of painting the whole path, without two consecutive tiles being of the same color.

Example
For 6 tiles:
# color:   1  2  3  4
costs = [[ 1, 3, 4, 5],  #  tile 1
           ^
         [ 2, 3, 2, 3],  #   2
                 ^
         [ 3, 1, 4, 1],  #   3
              ^
         [ 2, 3, 1, 3],  #   4
           ^
         [ 5, 4, 2, 4],  #   5
                 ^
         [ 6, 1, 6, 6]]  #   6
              ^

Optimal painting: tile 1 with color 1, tile 2 with color 3, tile 3 with color 2, tile 4 with color 1, tile 5 with color 3, tile 6 with color 2.
Total cost is costs[0][0] + costs[1][2] + costs[2][1] + costs[3][0] + costs[4][2] + costs[5][1] == 1+2+1+2+2+1 == 9.'''

def getpathcost_brute(costs, stepnum, laststep):

    if stepnum == len(costs):
        return 0

    mincost = 9999
    for c in range(len(costs[stepnum])):
        # print ("trying " + str(c))
        if c == laststep:
            # print ("skipping same")
            continue

        thiscost = costs[stepnum][c] + getpathcost_brute(costs, stepnum + 1, c)
        # print ("thiscost: " + str(thiscost))
        if thiscost < mincost:
            mincost = thiscost
            # print ("mincost: " + str(mincost))

    return mincost

def getpathcost_memo(costs, stepnum, laststep, savedcosts):

    if stepnum == len(costs):
        return 0

    mincost = 9999
    for c in range(len(costs[stepnum])):
        if c == laststep:
            continue

        if savedcosts[stepnum][c] > 0:
            thiscost = savedcosts[stepnum][c]
        else:
            thiscost = costs[stepnum][c] + getpathcost_memo(costs, stepnum + 1, c, savedcosts)
            savedcosts[stepnum][c] = thiscost

        if thiscost < mincost:
            mincost = thiscost

    return mincost

def getpathcost_matrix(costs):

    costmatrix = [[0 for x in range(4)] for y in range(len(costs) + 1)]
    costmatrix[0] = costs[0]
    print(costmatrix[0])
    for step in range(1, len(costs)):
        costmatrix[step][0] = costs[step][0] + min(costmatrix[step-1][1], costmatrix[step-1][2], costmatrix[step-1][3])
        costmatrix[step][1] = costs[step][1] + min(costmatrix[step-1][0], costmatrix[step-1][2], costmatrix[step-1][3])
        costmatrix[step][2] = costs[step][2] + min(costmatrix[step-1][0], costmatrix[step-1][1], costmatrix[step-1][3])
        costmatrix[step][3] = costs[step][3] + min(costmatrix[step-1][0], costmatrix[step-1][1], costmatrix[step-1][2])

        print(costmatrix[step])

    return(min(costmatrix[step][0], costmatrix[step][1], costmatrix[step][2], costmatrix[step][3]))

# should == 5
costinput2 = [[1,3,4,5], 
         [2,3,2,3], 
         [3,1,4,1],
         [2,3,1,3]]

# should == 9
costinput1 = [[ 1, 3, 4, 5],  #  tile 1
         [ 2, 3, 2, 3],  #   2
         [ 3, 1, 4, 1],  #   3
         [ 2, 3, 1, 3],  #   4
         [ 5, 4, 2, 4],  #   5
         [ 6, 1, 6, 6]]  #   6

# should == 20
costinput3 = [[2, 10, 4, 1],
          [10, 7, 10, 3],
          [6, 7, 10, 7],
          [9, 7, 6, 10],
          [4, 2, 7, 10],
          [9, 4, 1, 5]]


costinput = costinput1
savedcosts = [[-1 for x in range(len(costinput[0]) + 1)] for y in range(len(costinput))]

print(getpathcost_memo(costinput, 0, -1, savedcosts))

costinput = costinput1
print(getpathcost_matrix(costinput))