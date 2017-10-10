
def insertion_sort(alist):
    
    newlist = [alist[0]]
    alist.pop(0)
    for item in alist:
        last = True
        for i in range(0, len(newlist)):
            if item <= newlist[i]:
                newlist.insert(i, item)
                last = False
                break
        if (last == True):
            newlist.append(item)

    return newlist

# create a list of random numbers up to maximum_value
maximum_value = 1000000
length_of_list = 10000

from random import sample
alist = sample(range(maximum_value), length_of_list)
# alist = [2, 1, 3]

# start the timer
import time
start_time = time.clock()

sorted = insertion_sort(alist)

print ("It took " + str(time.clock() - start_time) + " seconds")

# print (sorted)
