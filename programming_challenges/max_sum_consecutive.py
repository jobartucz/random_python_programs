# find the largest sum of consecutive integers in an array
# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python

problem = '''The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.'''


import sys

def max_brute(arr):

    if len(arr) == 0:
        return 0

    if max(arr) < 0:
        return 0
    
    if min(arr) >= 0:
        return sum(arr)

    maxs = 0
    maxe = 0
    maxv = arr[0]

    for i in range(len(arr)):
        thismax = 0
        for j in range(i, len(arr)):
            thismax += arr[j]
            if thismax > maxv:
                maxs = i
                maxe = j + 1
                maxv = thismax

    return maxv
    # return arr[maxs:maxe]

def max_sequence(arr):

    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max

print(max_brute([-2, 1, -3, 4, -1, 2, 1, -5, 4]))