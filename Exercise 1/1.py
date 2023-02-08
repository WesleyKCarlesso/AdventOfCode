f = open(r"C:\Users\ninja\Documents\Programas\Python\AOC\AdventureOfCode\Exercise 1\input.txt")

list = f.readlines()

maxValue = 0
sum = 0

for i in list:
    line = i.split('\n')

    if (line[0] != ''):
        sum += int(i.split('\n')[0])
    else:
        if (sum > maxValue):
            maxValue = sum
        sum = 0

if (sum > maxValue):
    maxValue = sum

print('The largest value in list is:', maxValue)