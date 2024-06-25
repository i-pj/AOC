with open("input.txt") as f:
    ls = f.read().strip().split("\n")

board = {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}
blocked = {loc for loc, val in board.items() if val == "#"}
rounds = {loc for loc, val in board.items() if val == "O"}

while True:
    free = board.keys() - rounds - blocked
    newrounds = {z - 1 if z - 1 in free else z for z in rounds}
    if newrounds == rounds:
        break
    rounds = newrounds

print(sum(100 - z.real for z in rounds))
