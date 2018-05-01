#Find gcd of numbers a and b.
a = int(input('First Number: '))
b = int(input('First Number: '))

def gcd(a,b):
    if (a>b):
        temp = b
        b = a
        a = temp
    while (b%a!=0):
        r = b%a
        b = a
        a = r
        if (a>b):
            temp = b
            b = a
            a = temp
    return a

print(gcd(a,b))
