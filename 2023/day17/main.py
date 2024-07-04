import heapq
import numpy as np

def read_input(filename):
    with open(filename, 'r') as f:
        return np.array([list(map(int, line.strip())) for line in f.readlines()])

def dijkstra(grid):
    rows, cols = grid.shape
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = [(0, 0, 0, -1, 0)]
    visited = set()

    while queue:
        heat_loss, x, y, prev_dir, steps = heapq.heappop(queue)

        if (x, y) == (rows - 1, cols - 1) and steps >= 1:
            return heat_loss

        if (x, y, prev_dir, steps) in visited:
            continue
        visited.add((x, y, prev_dir, steps))

        for new_dir, (dx, dy) in enumerate(directions):
            if new_dir == (prev_dir + 2) % 4:
                continue
            if new_dir == prev_dir and steps == 3:
                continue
            if new_dir != prev_dir and steps < 1 and prev_dir != -1:
                continue

            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                new_steps = 1 if new_dir != prev_dir else steps + 1
                new_heat_loss = heat_loss + grid[nx, ny]
                heapq.heappush(queue, (new_heat_loss, nx, ny, new_dir, new_steps))

    return -1

grid = read_input('input.txt')
print(dijkstra(grid))
