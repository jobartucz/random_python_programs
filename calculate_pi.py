import math
import random

pi = 0
pi2 = 3

for i in range (1,10):
    
    # formula 1
    pi = pi + (((-1)**(i+1)*4) / (2*i-1))

    # formula 2
    pi2 = pi2 + ((-1)**(i + 1) * 4) / ((i*2)*((i*2)+1)*((i*2)+2))

print ("Formula 1:")
print (pi, pi - math.pi)
print ("Formula 2:")
print (pi2, pi2 - math.pi)

radius = 1000000;
total_darts = 100;
darts_in_circle = 0;

for i in range (1,total_darts):

    x = random.randrange(-1 * radius, radius)
    y = random.randrange(-1 * radius, radius)

    # is the dart in the circle?
    if (x * x + y * y <= radius * radius):
        darts_in_circle += 1;

# our estimate of pi according to the ratio of darts in the circle vs all darts
pi3 = 4 * (darts_in_circle / total_darts);

print ("Darts:")
print (pi3, pi3 - math.pi)

