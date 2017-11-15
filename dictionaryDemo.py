#Jack Robey
#11/15/17
#dictionaryDemo.py - list practice

dictionary = ['alphabet','sweatshirt','sweatpants','shorts','computer','water']

dictionary.sort()

number = int(input('What number word do you want to look up? '))
if number > len(dictionary):
    print('Invalid')
else:
    print('Word number', number, 'is', dictionary[number-1])