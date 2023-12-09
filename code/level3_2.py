filename = "inputs\level3_input.txt"

priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = 0

with open(filename) as file:
    i = 1
    badges = set()
    for line in file:
        rugsack = line.rstrip()
        if (i - 1) % 3 == 0:
            badges = set(rugsack)
        badges = set(rugsack).intersection(badges)

        if i % 3 == 0:
            total += sum([(priority.index(elem) + 1) for elem in badges])
        i += 1


print(total)
