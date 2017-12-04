#Jack Robey
#11/27/17
#selectionSort.py - implementation of selection sort

from random import randint
from time import time

N = 100 #how many numbers will be sorted

#Selection Sort
def mySort(a):
    n = len(a) 
    
    for j in range(0,n-1): 
        iMin = j 
        for i in range(j+1,n): 
            if a[i] < a[iMin]: 
                iMin = i
        if iMin != j: 
            a[j],a[iMin] = a[iMin],a[j]
    return a

if __name__ == '__main__':
    
    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
        
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers)
    t2 = time()
       
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
