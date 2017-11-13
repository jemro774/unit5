#Jack Robey
#11/13/17
#wordSort.py - asks the user for a list of words and then prints them alphabetically

words = input('Enter a list of words: ').split(' ')

words.sort()

for w in words:
    print(w)

