with open('input.txt', 'r') as f:
    grid = [list(line.strip()) for line in f.readlines()]
beams = [(0, 0, 0, 1)]  # (x, y, dx, dy)
energized = set()
while beams:
    new_beams = []
    for x, y, dx, dy in beams:
        if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
            if (x, y) not in energized:
                energized.add((x, y))
            if grid[y][x] == '.':
                new_beams.append((x + dx, y + dy, dx, dy))
            elif grid[y][x] in ['/', '\\']:
                if grid[y][x] == '/':
                    dx, dy = -dy, dx
                else:
                    dx, dy = dy, -dx
                new_beams.append((x + dx, y + dy, dx, dy))
            elif grid[y][x] in ['|', '-']:
                if dx == 0:
                    new_beams.append((x + 1, y, 1, 0))
                    new_beams.append((x - 1, y, -1, 0))
                else:
                    new_beams.append((x, y + 1, 0, 1))
                    new_beams.append((x, y - 1, 0, -1))
        else:
            continue
    beams = new_beams
print(len(energized))
