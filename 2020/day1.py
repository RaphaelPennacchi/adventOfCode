import sys

def a():
    entries = [int(entry.split('\n')[0]) for entry in sys.stdin if entry != '\n']
    for i in range(len(entries)):
        for j in range(i+1, len(entries)):
            if entries[i] + entries[j] == 2020:
                print(entries[i] * entries[j])
                return

def b():
    entries = [int(entry.split('\n')[0]) for entry in sys.stdin if entry != '\n']
    for i in range(len(entries)):
        for j in range(i+1, len(entries)):
            for k in range(j+1, len(entries)):
                if entries[i] + entries[j] + entries[k] == 2020:
                    print(entries[i] * entries[j] * entries[k])
                    return


b()
