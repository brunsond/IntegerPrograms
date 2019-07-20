#Calculates the partitions y of integer x, including the single partition.

#e.g. The partitions of x = 4 are:
#4
#3  1
#2  2
#2  1   1
#1  1   1   1
#So, y(4) = 5.

import numpy as np
x = int(input('Enter value: '))
j = 1
poly = np.array([1])   #Generating function polynomial.
while (j <= x):
    new_factor = []
    new_factor.append(1)
    num_sets = x//j
    i = 1
    k = 1
    while (k <= num_sets):
        new_factor[i:i+(j-1)] = (j-1)*[0]+[1]
        k = k+1
        i = i+j
    new_factor.reverse()
    nf = np.array(new_factor)
    poly = np.convolve(poly,nf)
    j = j+1
print(poly[len(poly)-1-x])
