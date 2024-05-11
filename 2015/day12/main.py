import json

def sum_numbers(obj, ignore_red=False):
    total = 0
    if isinstance(obj, list):
        for item in obj:
            total += sum_numbers(item, ignore_red)
    elif isinstance(obj, dict):
        if ignore_red and "red" in obj.values():
            return 0
        for key, value in obj.items():
            total += sum_numbers(value, ignore_red)
    elif isinstance(obj, int) or isinstance(obj, float):
        total += obj
    return total

with open('input.txt', 'r') as f:
    json_data = json.load(f)

# Part 1
result_part1 = sum_numbers(json_data)
print("Part 1 result:", result_part1)

# Part 2
result_part2 = sum_numbers(json_data, ignore_red=True)
print("Part 2 result:", result_part2)