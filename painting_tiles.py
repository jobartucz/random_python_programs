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

