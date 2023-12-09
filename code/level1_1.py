filename = "inputs\level1_input.txt"

totals = []

with open(filename) as file:
    elf_cal = []
    for line in file:
        cal = line.rstrip()
        if cal == "":
            totals.append(sum(map(int, elf_cal)))
            elf_cal = []
        else:
            elf_cal.append(cal)

print(totals)
print(max(totals))
