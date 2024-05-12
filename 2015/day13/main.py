import itertools

def read_input(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    guests = {}
    for line in lines:
        words = line.split()
        guest1 = words[0]
        happiness = int(words[3])
        if words[2] == 'lose':
            happiness = -happiness
        guest2 = words[10][:-1]
        if guest1 not in guests:
            guests[guest1] = {}
        guests[guest1][guest2] = happiness
    return guests

def calculate_happiness(guests, arrangement):
    total_happiness = 0
    for i in range(len(arrangement)):
        guest1 = arrangement[i]
        guest2 = arrangement[(i+1)%len(arrangement)]
        total_happiness += guests[guest1].get(guest2, 0)
        total_happiness += guests[guest2].get(guest1, 0)
    return total_happiness

def find_optimal_arrangement(guests):
    optimal_happiness = float('-inf')
    optimal_arrangement = None
    for arrangement in itertools.permutations(guests.keys()):
        happiness = calculate_happiness(guests, arrangement)
        if happiness > optimal_happiness:
            optimal_happiness = happiness
            optimal_arrangement = arrangement
    return optimal_happiness, optimal_arrangement

guests = read_input('input.txt')
optimal_happiness, optimal_arrangement = find_optimal_arrangement(guests)
print('Optimal happiness:', optimal_happiness)
print('Optimal arrangement:', optimal_arrangement)