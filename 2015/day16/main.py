import re

# Read the input file
with open('input.txt', 'r') as f:
    aunts = [line.strip() for line in f.readlines()]

# Parse the aunts' information
aunts_info = {}
for i, line in enumerate(aunts):
    aunt_info = {}
    matches = re.findall(r'(\w+): (\d+)', line)
    for match in matches:
        aunt_info[match[0]] = int(match[1])
    aunts_info[i+1] = aunt_info

# Define the gift's properties
gift = {
    'children': 3,
    'cats': 7,
   'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

# Find the matching aunt
for aunt, info in aunts_info.items():
    match = True
    for key, value in gift.items():
        if key in info and info[key]!= value:
            match = False
            break
    if match:
        print(aunt)
        break