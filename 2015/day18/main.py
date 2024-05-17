import numpy as np

def count_neighbors(grid, i, j):
    count = 0
    for x in range(max(0, i-1), min(100, i+2)):
        for y in range(max(0, j-1), min(100, j+2)):
            if (x, y)!= (i, j) and grid[x, y] == 1:
                count += 1
    return count

def step(grid, stuck_corners=False):
    new_grid = np.copy(grid)
    for i in range(100):
        for j in range(100):
            if stuck_corners and ((i, j) in [(0, 0), (0, 99), (99, 0), (99, 99)]):
                new_grid[i, j] = 1
            else:
                neighbors = count_neighbors(grid, i, j)
                if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                    new_grid[i, j] = 0
                elif grid[i, j] == 0 and neighbors == 3:
                    new_grid[i, j] = 1
    return new_grid

def solve(initial_grid, stuck_corners=False):
    grid = np.array([[1 if c == '#' else 0 for c in row] for row in initial_grid.splitlines()])
    if stuck_corners:
        grid[0, 0] = grid[0, 99] = grid[99, 0] = grid[99, 99] = 1
    for _ in range(100):
        grid = step(grid, stuck_corners)
    return np.sum(grid)

with open('input.txt') as f:
    initial_grid = f.read()

print("Part 1:", solve(initial_grid))
print("Part 2:", solve(initial_grid, stuck_corners=True))