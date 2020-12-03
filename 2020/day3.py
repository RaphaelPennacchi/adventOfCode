import sys

def a():
    total, place = 0, 0
    for line in sys.stdin:
        if line[place] == '#':
            total += 1
        place += 3
        place %= len(line) - 1
    print(total)


def look(mapa, right, down):
    x, y, total = 0, 0, 0
    while y < len(mapa):
        if mapa[y][x] == '#':
            total += 1
        x += right
        x %= len(mapa[y])
        y += down
    return total


def b():
    mapa = []
    for line in sys.stdin:
        mapa.append(line[:-1])
    total = [look(mapa, 1, 1),
             look(mapa, 3, 1),
             look(mapa, 5, 1),
             look(mapa, 7, 1),
             look(mapa, 1, 2)
             ]
    print(total)
    result = 1
    for number in total:
        result *= number
    print(result)


b()
