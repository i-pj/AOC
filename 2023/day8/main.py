import re

with open('input.txt', 'r') as f:
    maps = [line.strip() for line in f.readlines()]

graph = {}
for line in maps:
    match = re.match(r'(\w+) = \((\w+), (\w+)\)', line)
    if match:
        node, left, right = match.groups()
        graph[node] = (left, right)

instructions = re.search(r'([LR]+)', maps[0]).group(0)
instructions = instructions * (len(graph) * len(instructions))

current_node = 'AAA'
steps = 0
for instruction in instructions:
    left, right = graph[current_node]
    current_node = right if instruction == 'R' else left
    steps += 1
    if current_node == 'ZZZ':
        break

print(steps)
