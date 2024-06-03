from functools import reduce

with open("input.txt") as f:
    data = f.read().strip()

seed_line, *maps = data.split("\n\n")
seeds = list(map(int, seed_line.split(":")[1].split()))

fs = []
for m in maps:
    ns = [list(map(int, l.split())) for l in m.split("\n")[1:]]
    def f(x, ns=ns):
        return next((target + x - source for target, source, n in ns if source <= x < source + n), x)
    fs.append(f)

def compose(*F):
    return reduce(lambda f, g: lambda x: f(g(x)), F)

# Part 1
print(min(map(compose(*fs[::-1]), seeds)))
