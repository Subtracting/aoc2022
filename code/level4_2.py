filename = "inputs\level4_input.txt"

count = 1000

with open(filename) as file:
    for line in file:
        ranges = line.rstrip().split(",")
        elf_1_start, elf_1_end = list(map(int, ranges[0].split("-")))
        elf_2_start, elf_2_end = list(map(int, ranges[1].split("-")))

        if (elf_1_end < elf_2_start) or (elf_2_end < elf_1_start):
            count -= 1

print(count)
