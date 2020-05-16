
import heapq

class maxheap: # this is not done because I chose to use heapq
    # could have copied the code from here: https://www.geeksforgeeks.org/max-heap-in-python/

    def __init__(self, k):

        self.arr = [] * (k + 1)
        self.size = 0
        self.k = k

    def insert(self, num):

        if self.size == k:
            # if it's bigger than the current kth biggest, skip it
            if num > self.arr[0]:
                return
            


        for i in range(k + 1):
            if self.arr[i] == None:
                self.arr[i] = num
                heapify(i)

def kth_biggest(k, arr):

    if k <= 0 or k > len(arr):
        return None

    arr = [-1 * i for i in arr]

    myheap = arr[0:k]
    heapq.heapify(myheap)

    for num in arr[k:]:
        if num > arr[0]:
            heapq.heapreplace(myheap,num)

    return myheap[0] * -1



def kth_biggest_sorted(k, arr):
    
    if k <= 0 or k > len(arr):
        return None

    arr.sort()
    return arr[k-1]

def kth_biggest_def_qs(k, l):

    if len(l) <= 1:
        return l

    # we'll always choose the last element as the pivot
    pivot = l[randint(0, len(l) - 1)]

    print(pivot)

    a = []
    b = []
    for i in l:
        if i < pivot:
            a.append(i)
        else:
            b.append(i)

    if len(a) < k:
        return kth_biggest_def_qs(k, a) + kth_biggest_def_qs(k, b)
    else:
        kth_biggest_def_qs(k,a)

print(kth_biggest(4,[9,12,0,5,4,54323452345,8,7,6,5,4,3,2,1]))