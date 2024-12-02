with open("input.txt", "r") as f:
    data = f.readlines()

count1 = 0
count2 = 0

for report in data:
    levels = list(map(int, report.split()))
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    if all(1 <= abs(d) <= 3 for d in differences) and (
        all(d > 0 for d in differences) or all(d < 0 for d in differences)
    ):
        count1 += 1
        count2 += 1
    else:
        for i in range(len(levels)):
            temp_levels = levels[:i] + levels[i + 1 :]
            differences = [
                temp_levels[j + 1] - temp_levels[j] for j in range(len(temp_levels) - 1)
            ]
            if all(1 <= abs(d) <= 3 for d in differences) and (
                all(d > 0 for d in differences) or all(d < 0 for d in differences)
            ):
                count2 += 1
                break

print(count1)
print(count2)
