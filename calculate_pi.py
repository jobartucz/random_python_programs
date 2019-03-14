import math
import random

pi = 0
pi2 = 3

radius = 1000000;
darts = 0;
darts_in_circle = 0;

for i in range (1,10):
    
    # formula 1
    pi = pi + (((-1)**(i+1)*4) / (2*i-1))

    # formula 2
    pi2 = pi2 + ((-1)**(i + 1) * 4) / ((i*2)*((i*2)+1)*((i*2)+2))
    
    # darts!
    x = random.randrange(-1 * radius, radius)
    y = random.randrange(-1 * radius, radius)
    
    darts += 1
    if (x * x + y * y <= radius * radius):
        darts_in_circle += 1;

pi3 = 4 * (darts_in_circle / darts);

print ("Formula 1:")
print (pi, pi - math.pi)
print ("Formula 2:")
print (pi2, pi2 - math.pi)
print ("Darts:")
print (pi3, pi3 - math.pi)
