#Find lcm of numbers a and b.
#Employs Euclidean Algorithm.
a = int(input('First Number: '))
b = int(input('First Number: '))

def lcm(a,b):
    A = a
    B = b;
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
    return (A*B)/a


print(lcm(a,b))
