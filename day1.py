"""
data = []

with open('elves.txt') as file:
    calories = 0

    for line in file.readlines():
        line = line.strip()
        if line == '':
            data.append(calories)
            calories = 0
        else:
            calories += int(line)
print("Part 1 solution: ", max(data))
"""

with open('elves.txt', 'r') as f:
    input = f.readlines()

elf_total_calories = []
calories = []

for el in input:
    try:
        calories.append(int(el))
    except:
        elf_total_calories.append(sum(calories))
        calories = []

print(max(elf_total_calories))

#part two
print(sum(sorted(elf_total_calories, reverse=True)[:3]))