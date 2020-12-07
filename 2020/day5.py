file = open("day5.txt")

def part1():
    total = 0
    for line in file:
        toBin = ""
        for bit in line[:-1]:
            if bit in ["F", "L"]:
                toBin += "0"
            else:
                toBin += "1"
        if (holder := int(toBin[:7], 2) * 8 + int(toBin[7:], 2)) > total:
            total = holder
    print(total)

def part2():
    lista = []
    for line in file:
        toBin = ""
        for bit in line[:-1]:
            if bit in ["F", "L"]:
                toBin += "0"
            else:
                toBin += "1"
        lista.append(int(toBin[:7], 2) * 8 + int(toBin[7:], 2))
    lista.sort()
    size = len(lista)
    for i, value in enumerate(lista):
        if i != size -1 and value + 2 == lista[i+1]:
            print((value + lista[i+1]) // 2)

part2()
