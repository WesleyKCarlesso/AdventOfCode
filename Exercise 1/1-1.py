import sys

list = []

for line in sys.stdin:
    list.append(line.rstrip())

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