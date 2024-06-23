# import itertools
# 
# total_arrangements = 0
# with open('input.txt') as f:
#     for row in f:
#         springs, groups = row.strip().split()
#         groups = list(map(int, groups.split(',')))
#         unknowns = springs.count('?')
#         arrangements = 0
#         for p in itertools.product('.#', repeat=unknowns):
#             new_springs = list(springs)
#             i = 0
#             for j, c in enumerate(new_springs):
#                 if c == '?':
#                     new_springs[j] = p[i]
#                     i += 1
#             broken_groups = []
#             current_group = 0
#             for c in new_springs:
#                 if c == '#':
#                     current_group += 1
#                 else:
#                     if current_group > 0:
#                         broken_groups.append(current_group)
#                         current_group = 0
#             if current_group > 0:
#                 broken_groups.append(current_group)
#             if broken_groups == groups:
#                 arrangements += 1
#         total_arrangements += arrangements
# 
# print(total_arrangements)


import itertools

total_arrangements = 0
with open('input.txt') as f:
    for row in f:
        springs, groups = row.strip().split()
        groups = list(map(int, groups.split(',')))

        springs = '?'.join([springs] * 5)
        groups = groups * 5

        unknowns = springs.count('?')
        arrangements = 0
        for p in itertools.product('.#', repeat=unknowns):
            new_springs = list(springs)
            i = 0
            for j, c in enumerate(new_springs):
                if c == '?':
                    new_springs[j] = p[i]
                    i += 1
            broken_groups = []
            current_group = 0
            for c in new_springs:
                if c == '#':
                    current_group += 1
                else:
                    if current_group > 0:
                        broken_groups.append(current_group)
                        current_group = 0
            if current_group > 0:
                broken_groups.append(current_group)
            if broken_groups == groups:
                arrangements += 1
        total_arrangements += arrangements

print(total_arrangements)
