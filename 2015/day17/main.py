import itertools

def count_combinations(containers, target):
    count = 0
    min_containers = float('inf')
    min_ways = 0
    for r in range(1, len(containers) + 1):
        ways = 0
        for combination in itertools.combinations(containers, r):
            if sum(combination) == target:
                ways += 1
        if ways > 0 and r < min_containers:
            min_containers = r
            min_ways = ways
    return count, min_ways

with open('input.txt', 'r') as f:
    containers = [int(line.strip()) for line in f.readlines()]

part1 = 0
for r in range(1, len(containers) + 1):
    for combination in itertools.combinations(containers, r):
        if sum(combination) == 150:
            part1 += 1

_, part2 = count_combinations(containers, 150)

print("Part 1:", part1)
print("Part 2:", part2)