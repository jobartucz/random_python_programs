
# given an array, print out how many sub-arrays sum to a specific number:
# i.e: 
# sumsub([1,2,3,4,5],5) == 2 because you can add [2,3] and you already have [5]
# sumsub([1,1,1,1,1],3) == 3 because you have the first 3 ones, the second 3 ones and the third 3 ones

def sumsub_brute(l,n):

    num = 0
    for i in range(len(l)):
        for j in range(i+1, len(l)+1):
            sum = 0
            for k in range(i,j):
                sum += l[k]
                # can't do this because we might have negatives 
                # if sum > n:
                #    break
            if sum == n:
                num += 1

    return num

print(sumsub_brute([1,1,1,1,1], 5))
