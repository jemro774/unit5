#Jack Robey
#11/17/17
#randomMonth.py - prints out a random month of the year

from random import randint

months = ['January','February','March','April','May','June','July','August','September','October','November','December']
print(randint(months[0],months[11]))
