#Jack Robey
#11/16/17
#warmup13 - makes a list of 20 random numbers and does stuff with it

from random import randint

numbers = []

for i in range(1,21):
    numbers.append(randint(1,101))
    
print(min(numbers))
print(max(numbers))
print(sum(numbers))
    
