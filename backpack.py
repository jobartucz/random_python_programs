instructions = '''
To make sure you're bringing your most valuable items on this journey you've decided to give all your items a score that represents how valuable this item is to you. It's your job to pack you bag so that you get the most value out of the items that you decide to bring.

Your input will consist of two arrays, one for the scores and one for the weights. You input will always be valid lists of equal length, so you don't have to worry about verifying your input.

You'll also be given a maximum weight. This is the weight that your backpack cannot exceed.

For instance, given these inputs:

scores = [15, 10, 9, 5]
weights = [1, 5, 3, 4]
capacity = 8

The maximum score will be 29. This number comes from bringing items 1, 3 and 4.

Note: Your solution will have to be efficient as the running time of your algorithm will be put to a test.'''


def packval(s, w, c, n):

    if n < 0 or w == 0:
        return 0
    if w[n] > c:
        return packval(s, w, c, n-1)

    scorewith = s[n] + packval(s, w, c - w[n], n - 1)
    scorewithout = packval(s, w, c, n-1)
    return max(scorewith, scorewithout)


def packval_optimized(s, w, c, n, optlist):
    if n < 0 or w == 0:
        return 0

    if w[n] > c:
        return packval_optimized(s, w, c, n-1, optlist)

    if optlist[n][c] >= 0:
        return optlist[n][c]

    scorewith = s[n] + packval_optimized(s, w, c - w[n], n - 1, optlist)
    scorewithout = packval_optimized(s, w, c, n-1, optlist)
    optlist[n][c] = max(scorewith, scorewithout)
    return max(scorewith, scorewithout)


def packval_dynamic(cap, wt, val, n):
    K = [[0 for x in range(cap + 1)] for y in range(n + 1)]
    # Table in bottom up manner
    for i in range(n + 1):
        for w in range(cap + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
        
            print(K[i][w], end=" ")
        print()

    return K[n][cap]


scores = [15, 10, 9, 5]
weights = [1, 5, 3, 4]
capacity = 8

scores = [20, 5, 10, 40, 15, 25]
weights = [1, 2, 3, 8, 7, 4]
capacity = 10

# zero out the optlist
optlist = []
for i in range(len(scores)):
    optlist.append([])
    for j in range(capacity+1):
        optlist[i].append(-1)

# print(packval(scores, weights, capacity, len(weights) - 1))
# print(packval_optimized(scores, weights, capacity, len(weights) - 1, optlist))
print(packval_dynamic(capacity, weights, scores, len(weights)))
