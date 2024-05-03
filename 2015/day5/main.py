#part 1
def is_nice(s):
    vowels = 'aeiou'
    if sum(c in vowels for c in s) < 3:
        return False
    if not any(s[i] == s[i+1] for i in range(len(s)-1)):
        return False
    if any(bad in s for bad in ['ab', 'cd', 'pq', 'xy']):
        return False
    return True

with open('input.txt') as f:
    nice_count = sum(1 for line in f if is_nice(line.strip()))

print(nice_count)

#part 2
def is_nice(s):
    if not any(s[i:i+2] in s[i+2:] for i in range(len(s)-1)):
        return False
    if not any(s[i] == s[i+2] for i in range(len(s)-2)):
        return False
    return True

with open('input.txt') as f:
    nice_count = sum(1 for line in f if is_nice(line.strip()))

print(nice_count)