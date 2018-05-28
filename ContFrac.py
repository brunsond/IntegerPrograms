import math

# Prints out a list of the first N coefficients for the continued
# fraction expansion of the square root of n for n irrational.

# Prints None if n is a perfect square.

n = float(input("Enter the number n so that the cont'd fraction is for sqrt(n). "))
N = int(input("Enter the number of desired terms for the cont'd fraction expansion. "))

def contFrac(n,N):
    if (math.sqrt(n)==math.floor(math.sqrt(n))):
        pass
    else:
        m = 0
        d = 1
        a0 = math.floor(n**0.5)
        a = a0
        myList = []
        for i in range(1,N+1):
            m = d*a-m
            d = (n-m**2)/d
            a = math.floor((a0+m)/d)
            myList.append(a)
        return myList

print(contFrac(n,N))
