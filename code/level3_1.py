filename = "inputs\level3_input.txt"

priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = 0

print(len(priority))

with open(filename) as file:
    for line in file:
        rugsack = line.rstrip()
        half = len(rugsack) // 2
        first = rugsack[:half]
        second = rugsack[half:]
        both = set(first).intersection(set(second))
        total += sum([(priority.index(elem) + 1) for elem in both])

print(total)
