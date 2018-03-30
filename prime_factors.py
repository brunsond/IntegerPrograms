# Prints the prime factorization of a positive integer >= 2.
# The code is fast for integers 5 digits or fewer.
# Runs as is with Python3 interpreter.

# Written by Douglas Brunson (2018).

#############################################################
n = int(input("Enter integer: "))
if n < 2:
    print('Integer must be greater than or equal to 2.')
else:
    val = True
    for j in range(2,int(n**0.5)+1):
        if n % j == 0:
            val = False
            continue
    if val:
        print(n)
    else:
        primes = [2]
        if n%2==0:
	        d = 2
        else:
	        d = 3
        for i in range(3,int(n/d)+1):
            val = True
            for j in range(2,int(i**0.5)+1):
	            if i % j == 0:
	                val = False
	                continue
            if val:
	            primes.append(i)
        while n>1:
            for p in primes:
            	while n%p == 0:
	                n /= p
	                print(p)
#############################################################



