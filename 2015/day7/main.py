with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

index = {line.split()[-1]: line for line in lines}

def evaluate_wire(wire, cache):
    if wire.isdigit():
        return int(wire)
    if wire in cache:
        return cache[wire]
    line = index[wire]
    words = line.split()
    if words[1] == '->':
        result = evaluate_wire(words[0], cache)
    elif words[0] == 'NOT':
        result = ~evaluate_wire(words[1], cache)
    elif words[1] == 'AND':
        result = evaluate_wire(words[0], cache) & evaluate_wire(words[2], cache)
    elif words[1] == 'OR':
        result = evaluate_wire(words[0], cache) | evaluate_wire(words[2], cache)
    elif words[1] == 'RSHIFT':
        result = evaluate_wire(words[0], cache) >> int(words[2])
    elif words[1] == 'LSHIFT':
        result = evaluate_wire(words[0], cache) << int(words[2])
    cache[wire] = result
    return result

# Part one
cache = {}
result = evaluate_wire('a', cache)
print(result)

# Part two
cache = {'b': result}
print(evaluate_wire('a', cache))