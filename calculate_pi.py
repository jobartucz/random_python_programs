import math

pi = 0
pi2 = 3

for i in range (1,100):
    
    pi = pi + (((-1)**(i+1)*4) / (2*i-1))

    pi2 = pi2 + ((-1)**(i + 1) * 4) / ((i*2)*((i*2)+1)*((i*2)+2))
    
print (pi, pi - math.pi)
print (pi2, pi2 - math.pi)
