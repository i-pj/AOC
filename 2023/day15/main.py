with open('input.txt', 'r') as f:
    initialization_sequence = f.read().strip()
steps = initialization_sequence.split(',')
results = []
for step in steps:
    current_value = 0
    for c in step:
        ascii_code = ord(c)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    results.append(current_value)
print(sum(results))
