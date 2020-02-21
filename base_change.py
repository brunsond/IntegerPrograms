# Converts decimal integer n to its equivalent in base b.
# Runs as is via python3 interpreter.

# Written by Douglas Brunson (2018).

###########################################################################
import math

b = float(input("Enter base (>=2): "))

if (b < 2):
    print('Error. Base must be >= 2.')
else:
    n = float(input("Enter decimal integer you wish to convert: "))
    if (b > n):
        print(int(n))
    else:
        r = math.floor(math.log(n)/math.log(b)) #Max value such that b^r <= n
        a = []  #List to store coefficients
        a.append(1)
        x = n - b**r
        while (x > b**r):
            a[0] += 1
            x -= b**r
        for i in range(1,r+1):
            if (b**(r-i) > x):
                a.append(0)
            else:
                a.append(0)
                while (x >= b**(r-i)):
                    a[i] += 1
                    x -= b**(r-i)
        for i in range(0,r+1):
            print(a[i],end=" ")
        print("\n")
###########################################################################
    





