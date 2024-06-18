from collections import deque

with open("input.txt", "r") as f:
    ls = f.read().strip().split("\n")

board = {(i, j): x for i, l in enumerate(ls) for j, x in enumerate(l)}
dirs = {
    "|": [(0, 1), (0, -1)],
    "-": [(1, 0), (-1, 0)],
    "J": [(-1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    "S": [(1, 0), (0, 1)],
    "7": [(1, 0), (0, -1)],
    "L": [(-1, 0), (0, 1)],
}
connections = {
    "F": ["-", "|"],
    "J": ["-", "7"],
    "7": ["-", "L"],
    "L": ["-", "F"],
    "|": ["J", "F"],
    "-": ["7", "L"],
}
S = next((z for z, x in board.items() if x == "S"), None)
board[S] = "F"
seen = {S}
q = deque([(S, 0)])
while q:
    z, dist = q.popleft()
    for dz in dirs[board[z]]:
        newz = (z[0] + dz[0], z[1] + dz[1])
        if newz not in seen and newz in board:
            next_pipe = board[newz]
            if next_pipe in connections[board[z]] or next_pipe == board[z]:
                q.append((newz, dist + 1))
                seen.add(newz)

# Part 1
print(max(dist for _, dist in seen))
