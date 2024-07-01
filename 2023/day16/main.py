from collections import deque
import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    grid = [line.strip() for line in file]

rows, cols = len(grid), len(grid[0])
energized = set()
beams = deque([(0, 0, 0, 1)])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while beams:
    r, c, dr, dc = beams.popleft()

    while 0 <= r < rows and 0 <= c < cols:
        energized.add((r, c))
        char = grid[r][c]

        if char == '/' or char == '\\':
            dr, dc = -dc, -dr
            if char == '\\':
                dr, dc = -dr, -dc
        elif char == '|' and dc != 0:
            beams.append((r, c, -1, 0))
            beams.append((r, c, 1, 0))
            break
        elif char == '-' and dr != 0:
            beams.append((r, c, 0, -1))
            beams.append((r, c, 0, 1))
            break

        r, c = r + dr, c + dc

print(f"Number of energized tiles: {len(energized)}")
