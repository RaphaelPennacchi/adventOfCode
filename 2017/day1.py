def a():
    numbers = input()
    total = 0
    for number in range(len(numbers)):
        if numbers[number-1] == numbers[number]:
            total += int(numbers[number])
    print(total)

def b():
    numbers = input()
    total = 0
    for number in range(len(numbers)):
        if numbers[number] == numbers[(number + len(numbers) // 2) % len(numbers)]:
            total += int(numbers[number])
    print(total)
