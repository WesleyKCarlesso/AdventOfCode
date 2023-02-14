import sys

lines = []

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line.rstrip())

print(lines)