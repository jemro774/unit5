#Jack Robey
#12/4/17
#quiz5.py

from random import randint

def rand5():
    x = []
    for i in range(1,6):
        x.append(randint(1,101))
    return x

def lastElement(y):
    return y[len(y)-1]

def biggest(z):
    z.sort()
    return z[len(z)-1]

print(rand5())
print(lastElement(['cat','dog','rat']))
print(biggest([3,-1,5,-2,7,2,1]))