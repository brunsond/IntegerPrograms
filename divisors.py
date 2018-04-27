#Prints out list of the divisors of a positive integer.

# Written by Douglas Brunson (2018).

n = float(input('Enter integer >= 1. '))
divisors = [1]
for i in range(2,int(n**0.5)+1):
    if (n%i==0):
        if (i!=n/i):
            divisors.append(i)
            divisors.append(int(n/i))
        else:
            divisors.append(i)
divisors.append(int(n))
divisors.sort()
print(divisors)
