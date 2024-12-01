with open("./input.txt", "r") as f:
    lines = f.readlines()
    l_list = []
    r_list = []

    for line in lines:
        l, r = map(int, line.strip().split())
        l_list.append(l)
        r_list.append(r)

distance = sum(abs(left - right) for left, right in zip(sorted(l_list), sorted(r_list)))
print(distance)

count = {}
for num in r_list:
    count[num] = count.get(num, 0) + 1

score = 0
for num in l_list:
    occurence = count.get(num, 0)
    score += num * occurence
print(score)
