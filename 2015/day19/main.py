import re
import random

def load_input(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    replacements = {}
    for line in lines[:-2]:
        pattern, replacement = line.strip().split(' => ')
        if pattern not in replacements:
            replacements[pattern] = []
        replacements[pattern].append(replacement)
    medicine = lines[-1].strip()
    return replacements, medicine

def generate_molecules(replacements, medicine):
    molecules = set()
    for pattern, replacement_list in replacements.items():
        for replacement in replacement_list:
            for match in re.finditer(pattern, medicine):
                start, end = match.start(), match.end()
                new_molecule = medicine[:start] + replacement + medicine[end:]
                molecules.add(new_molecule)
    return len(molecules)

def mutate(sq, replacements):
    for pos in range(len(sq)):
        for a, b_list in replacements.items():
            if sq[pos:].startswith(a):
                for b in b_list:
                    yield sq[:pos] + b + sq[pos+len(a):]

def search(mol, reps):
    target = mol
    mutations = 0
    while target!= 'e':
        tmp = target
        for a, b_list in reps:
            for b in b_list:
                index = target.find(b)
                if index >= 0:
                    target = target[:index] + a + target[index + len(b):]
                    mutations += 1
        if tmp == target:
            target = mol
            mutations = 0
            random.shuffle(reps)
    return mutations

def main():
    replacements, medicine = load_input('input.txt')
    print("Part 1:", len(set(mutate(medicine, replacements))))
    print("Part 2:", search(medicine, list(replacements.items())))

if __name__ == "__main__":
    main()












































































