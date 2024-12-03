import re

with open("./input.txt", "r") as f:
    memory = f.read()

pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, memory)

total = sum(int(x) * int(y) for x, y in matches)
print(total)

# part2
control_pattern = r"(do\(\)|don't\(\))"
instructions = re.findall(f"{pattern}|{control_pattern}", memory)

enabled = True
total = 0

for instruction in instructions:
    if instruction[0] and instruction[1]:
        if enabled:
            total += int(instruction[0]) * int(instruction[1])
    elif instruction[2] == "do()":
        enabled = True
    elif instruction[2] == "don't()":
        enabled = False

print(total)
