with open('input.txt') as f:
    data = f.read().strip()

lines = data.split("\n")
times = list(map(int, [x for x in lines[0].split() if x.isdigit()]))
distances = list(map(int, [x for x in lines[1].split() if x.isdigit()]))

ways_to_win = 1

for t, d in zip(times, distances):
    count = 0
    for speed in range(1, t):
        total = (t - speed) * speed

        if total > d:
            count += 1

    ways_to_win *= count

print(ways_to_win)
