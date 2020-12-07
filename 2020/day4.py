import sys

fieldsRequired = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

file = open("day4.txt")

def checkFields(fieldsRequired, fields):
    for field in fieldsRequired:
        if field not in fields:
            return False
    return True

def a():
    fields = []
    total = 0
    for line in sys.stdin:
        if line == '\n':
            if checkFields(fieldsRequired, fields):
                total += 1
            fields.clear()
        else:
            for field in line[:-1].split(" "):

                fields.append(field.split(":")[0])
    if checkFields(fieldsRequired, fields):
        total += 1
    print(total)

def b():
    fields = []
    total = 0
    for line in file:
        if line == '\n':
            if checkFields(fieldsRequired, fields):
                total += 1
            fields.clear()
        else:
            for field in line[:-1].split(" "):
                fil, con = field.split(":")
                if fil == "byr":
                    if 1920 <= int(con) <= 2002:
                        fields.append(fil)
                elif fil == "iyr":
                    if 2010 <= int(con) <= 2020:
                        fields.append(fil)
                elif fil == "eyr":
                    if 2020 <= int(con) <= 2030:
                        fields.append(fil)
                elif fil == "hgt":
                    if con[-2:] == "in" and 59 <= int(con[:2]) <= 76:
                        fields.append(fil)
                    elif con[-2:] == "cm" and len(con) == 5 and  150 <= int(con[:3]) <= 193:
                        fields.append(fil)
                elif fil == "hcl":
                    if con[0] == "#" and len(con) == 7:
                        fields.append(fil)
                elif fil == "ecl":
                    if con in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        fields.append(fil)
                elif fil == "pid":
                    if len(con) == 9:
                        fields.append(fil)
    print(total)

b()
