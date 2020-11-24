import sys

def a():
    diff = []
    for line in sys.stdin:
        line = [int(number) for number in line.split(' ') if number != '']
        diff.append(max(line) - min(line))
    print(sum(diff))

def b():
    div = []
    for line in sys.stdin:
        line = [int(number) for number in line.split(' ') if number != '']
        line.sort()
        for i in range(len(line)):
            for j in range(i+1, len(line)):
                if line[j] % line[i] == 0:
                    div.append(line[j]//line[i])
                    break
    print(sum(div))
