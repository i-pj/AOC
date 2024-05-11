import json

with open('input.txt', 'r') as f:
    json_data = json.load(f)

def sum_numbers(obj):
    total = 0
    if isinstance(obj, list):
        for item in obj:
            total += sum_numbers(item)
    elif isinstance(obj, dict):
        for key, value in obj.items():
            total += sum_numbers(value)
    elif isinstance(obj, int) or isinstance(obj, float):
        total += obj
    return total

result = sum_numbers(json_data)
print(result)