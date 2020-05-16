
# mergesort

def mergesort(l):

    if len(l) <= 1:
        return l

    length = len(l) // 2

    a = l[:length]
    b = l[length:]

    a = mergesort(a)
    b = mergesort(b)

    c = []
    acounter = 0
    bcounter = 0
    while acounter < len(a) and bcounter < len(b):
        if a[acounter] < b[bcounter]:
            c.append(a[acounter])
            acounter += 1
        else:
            c.append(b[bcounter])
            bcounter += 1

    while acounter < len(a):
        c.append(a[acounter])        
        acounter += 1

    while bcounter < len(b):
        c.append(b[bcounter])
        bcounter += 1

    return c





print(mergesort([6,6,6,5,4,3,2,1,0]))