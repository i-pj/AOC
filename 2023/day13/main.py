import numpy as np

with open("input.txt") as f:
    patterns = f.read().strip().split("\n\n")

def find_mirror(a, mismatch):
    for i in range(1, len(a)):
        n = min(i, len(a) - i)
        if np.sum(a[:i][::-1][:n] ^ a[i:][:n]) == mismatch:
            return i
    return None

total = 0
for pattern in patterns:
    lines = pattern.split("\n")
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len, '.') for line in lines]
    a = np.array([[x == "#" for x in line] for line in lines])
    row_mirror = find_mirror(a, 0)
    col_mirror = find_mirror(a.T, 0)
    if row_mirror is not None:
        total += 100 * row_mirror
    elif col_mirror is not None:
        total += col_mirror
print(total)

