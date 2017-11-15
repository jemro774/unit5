#Jack Robey
#11/15/17
#middleWord.py - asks the user for a list of words then prints out the middle one

words = input('Enter some words: ').split(' ')

middleIndexing = len(words)//2

if len(words)%2 == 0:
    print(words[middleIndexing-1:middleIndexing+1])
else:
    print(words[middleIndexing])


