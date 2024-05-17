import numpy as np

def count_neighbors(grid, i, j):
    count = 0
    for x in range(max(0, i-1), min(100, i+2)):
        for y in range(max(0, j-1), min(100, j+2)):
            if (x, y)!= (i, j) and grid[x, y] == 1:
                count += 1
    return count

def step(grid):
    new_grid = np.copy(grid)
    for i in range(100):
        for j in range(100):
            neighbors = count_neighbors(grid, i, j)
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1
    return new_grid

def solve(initial_grid):
    grid = np.array([[1 if c == '#' else 0 for c in row] for row in initial_grid.splitlines()])
    for _ in range(100):
        grid = step(grid)
    return np.sum(grid)

with open('input.txt') as f:
    initial_grid = f.read()
print(solve(initial_grid))