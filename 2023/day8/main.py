import re
import math

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

instrs = maps[0].split()[0]
nodes = {}

current = []

for node in maps[1:]:
    src, left, right = re.findall(r"([A-Z0-9]{3})", node)
    nodes[src] = (left, right)

    if src[2] == "A":
        current.append(src)

lens = []
for v in current:
    node = v
    idx = 0

    t = 0
    while node[2]!= "Z":
        move = instrs[idx % len(instrs)]
        idx += 1
        node = nodes[node][0 if move == "L" else 1]
        t += 1

    lens.append(t)

print(math.lcm(*lens))
