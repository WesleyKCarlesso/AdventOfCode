import sys

list = []

for line in sys.stdin:
    list.append(line.rstrip())

firstMaxValue = 0
secondMaxValue = 0
thirdMaxValue = 0
sum = 0

for i in list:
    line = i.split('\n')

    if (line[0] != ''):
        sum += int(i.split('\n')[0])
    else:
        if (sum > firstMaxValue):
            thirdMaxValue = secondMaxValue
            secondMaxValue = firstMaxValue
            firstMaxValue = sum
        if (sum > secondMaxValue and sum < firstMaxValue):
            secondMaxValue = sum
        if (sum > thirdMaxValue and sum < secondMaxValue):
            thirdMaxValue = sum
        sum = 0
        
if (sum > firstMaxValue):
    thirdMaxValue = secondMaxValue
    secondMaxValue = firstMaxValue
    firstMaxValue = sum
if (sum > secondMaxValue and sum < firstMaxValue):
    secondMaxValue = sum
if (sum > thirdMaxValue and sum < secondMaxValue):
    thirdMaxValue = sum

total = firstMaxValue + secondMaxValue + thirdMaxValue

print('first:', firstMaxValue, ' second:', secondMaxValue, 'third:', thirdMaxValue)
print('The sum of three highest values is', total)