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

from collections import defaultdict 
from random import randint

def sumsub_rolling(l,n):

    if len(l) == 0:
        return 0
    if len(l) == 1:
        if l[0] == n: 
            return 1
        else:
            return 0

    # how many sums
    num = 0

    # the rolling sum of numbers
    rolling = []
    rolling.append(l[0]) # rolling sum starts with first number

    # create the hashmap
    hm = defaultdict(int)
    hm[0] = 1 # in case the whole thing sums to our number
    hm[l[0]] = 1 # add the first value to the map because we are starting at the second

    for i in range(1, len(l)):
        rolling.append(rolling[i-1] + l[i])
        if rolling[i] - n in hm: # if we have the complement, add the number of them to the total
            # print(f"There are {hm[rolling[i] - n]} complement(s) for {rolling[i]}")
            num += hm[rolling[i] - n]

        hm[rolling[i]] += 1


    # print(hm)


    return num

print(sumsub_rolling([1,2,3],0),78787878)
print(sumsub_rolling([],5),0)
print(sumsub_rolling([-1],-1), 1)
print(sumsub_rolling([15],15), 1)
print(sumsub_rolling([1,8,-3,8,5], 5), 3)
print(sumsub_rolling([1,2,3,4,5],5),2)
print(sumsub_rolling([1,2,4],5),0)
print(sumsub_rolling([1,1,1,1,1],3),3)
print(sumsub_rolling([1,8,-3,8,5],5),3)
print(sumsub_rolling([-1,8,-3,-8,5],-11),1)

testlist = [randint(-1000,1000) for i in range(100000)]

testresult1=sumsub_rolling(testlist, randint(-100,100))
testresult2=sumsub_rolling(testlist, randint(-100,100))
print()
print(testresult1, testresult2)