import heapq
import numpy as np


def read_input(filename):
    with open(filename, "r") as f:
        return np.array([list(map(int, line.strip())) for line in f.readlines()])


def dijkstra(grid, part):
    rows, cols = grid.shape
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = [(0, 0, 0, -1, 0)] if part == 1 else [(0, 0, 0, -1, 0, 0)]
    visited = set()

    while queue:
        heat_loss, x, y, prev_dir, steps = queue[0] if part == 1 else queue[0][:5]
        consec_steps = queue[0][5] if part == 2 else 0

        if (x, y) == (rows - 1, cols - 1) and steps >= 1:
            return heat_loss

        if (x, y, prev_dir, steps, consec_steps) in visited:
            continue
        visited.add((x, y, prev_dir, steps, consec_steps))

        for new_dir, (dx, dy) in enumerate(directions):
            if new_dir == (prev_dir + 2) % 4:
                continue
            if part == 1:
                if new_dir == prev_dir and steps == 3:
                    continue
                if new_dir != prev_dir and steps < 1 and prev_dir != -1:
                    continue
            else:
                if new_dir == prev_dir and consec_steps == 10:
                    continue
                if new_dir != prev_dir and consec_steps < 4 and prev_dir != -1:
                    continue

            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                new_consec_steps = (
                    consec_steps + 1 if new_dir == prev_dir else 1 if part == 2 else 0
                )
                new_steps = 1 if new_dir != prev_dir else steps + 1
                new_heat_loss = heat_loss + grid[nx, ny]
                if part == 1:
                    heapq.heappush(queue, (new_heat_loss, nx, ny, new_dir, new_steps))
                else:
                    heapq.heappush(
                        queue,
                        (new_heat_loss, nx, ny, new_dir, new_steps, new_consec_steps),
                    )

        heapq.heappop(queue)

    return -1


grid = read_input("input.txt")
print("Part 1:", dijkstra(grid, 1))
print("Part 2:", dijkstra(grid, 2))
