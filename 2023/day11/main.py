import numpy as np
import itertools

with open('input.txt', 'r') as f:
    data = [list(line.strip()) for line in f.readlines()]

data = np.array(data)

empty_rows = np.where(np.all(data == '.', axis=1))[0]
empty_cols = np.where(np.all(data == '.', axis=0))[0]

galaxies = np.where(data == '#')
galaxies = list(zip(galaxies[0], galaxies[1]))

total_distance = 0
for g1, g2 in itertools.combinations(galaxies, 2):
    empty_rows_between = len(np.intersect1d(range(min(g1[0], g2[0]), max(g1[0], g2[0])), empty_rows))
    empty_cols_between = len(np.intersect1d(range(min(g1[1], g2[1]), max(g1[1], g2[1])), empty_cols))

    distance = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) + empty_rows_between + empty_cols_between

    total_distance += distance

print(total_distance)

