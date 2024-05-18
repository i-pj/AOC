import re

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

replacements, medicine = load_input('input.txt')
print(generate_molecules(replacements, medicine))
