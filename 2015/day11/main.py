def increment_password(password):
    password = list(password)
    for i in range(len(password) - 1, -1, -1):
        if password[i] == 'z':
            password[i] = 'a'
        else:
            password[i] = chr(ord(password[i]) + 1)
            break
    return ''.join(password)

def has_increasing_straight(password):
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i+1]) and ord(password[i+1]) + 1 == ord(password[i+2]):
            return True
    return False

def has_confusing_letters(password):
    return any(c in password for c in 'iol')

def has_non_overlapping_pairs(password):
    pairs = []
    for i in range(len(password) - 1):
        if password[i] == password[i+1] and password[i] not in pairs:
            pairs.append(password[i])
        if len(pairs) >= 2:
            return True
    return False

def next_password(password):
    while True:
        password = increment_password(password)
        if not has_confusing_letters(password) and has_increasing_straight(password) and has_non_overlapping_pairs(password):
            return password

print(next_password('hepxcrrq'))


# Part 2
# Next password
part1_output = next_password('hepxcrrq')
print(next_password(part1_output))

