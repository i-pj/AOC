pwds = []
with open("input.txt") as f:
    for line in f:
        pwds.append((line.strip().split(" ")))


def is_valid(s):
    rng = s[0].split("-")
    ll, ul = int(rng[0]), int(rng[1])
    c = s[1][0]
    if ll <= s[2].count(c) <= ul:
        return True
    return False

is_valid(pwds[0])
count = 0
for pwd in pwds:
    if is_valid(pwd):
        count += 1

print(count)