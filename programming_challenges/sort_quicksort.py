
from random import randint

def qs(l):

    if len(l) <= 1:
        return l

    # we'll always choose the last element as the pivot
    pivot = l[randint(0, len(l) - 1)]

    # print(pivot)

    a = []
    b = []
    for i in l:
        if i < pivot:
            a.append(i)
        else:
            b.append(i)

    return qs(a) + qs(b)


print(qs([5,4,3,2,1,0]))