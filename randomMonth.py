#Jack Robey
#11/17/17
#randomMonth.py - prints out a random month of the year

from random import randint

months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Deciembre']
print(months[randint(0,11)])
