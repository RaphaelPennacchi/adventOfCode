import sys

def a():
    total = 0
    for line in sys.stdin:
        command, string = line.replace("-", " ").split(": ")
        command = command.split(" ")
        count = string.count(command[2])
        if int(command[0]) <= count <= int(command[1]):
            total += 1
    print(total)

def b():
    total = 0
    for line in sys.stdin:
        command, string = line.replace("-", " ").split(": ")
        command = command.split(" ")
        foo = 0
        if(string[int(command[0]) - 1] == command[2]):
            foo += 1
        if(string[int(command[1]) - 1] == command[2]):
            foo += 1
        if(foo == 1):
            total += 1
    print(total)

b()
