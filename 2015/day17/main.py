import itertools

def count_combinations(containers, target):
    count = 0
    for r in range(1, len(containers) + 1):
        for combination in itertools.combinations(containers, r):
            if sum(combination) == target:
                count += 1
    return count

with open('input.txt', 'r') as f:
    containers = [int(line.strip()) for line in f.readlines()]

print(count_combinations(containers, 150))