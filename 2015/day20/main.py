import math

def sum_of_divisors(n, max_visits, multiplier):
    sum = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i <= max_visits:
                sum += i * multiplier
            if n // i <= max_visits and i * i!= n:
                sum += n // i * multiplier
    return sum

def find_house_with_at_least_presents(presents_threshold, max_visits, multiplier):
    house_number = 1
    while True:
        if sum_of_divisors(house_number, max_visits, multiplier) >= presents_threshold:
            return house_number
        house_number += 1

puzzle_input = 29000000

# Part 1
result_part1 = find_house_with_at_least_presents(puzzle_input, float('inf'), 10)
print("The lowest house number to get at least", puzzle_input, "presents in Part 1 is:", result_part1)

# Part 2
result_part2 = find_house_with_at_least_presents(puzzle_input, 50, 11)
print("The lowest house number to get at least", puzzle_input, "presents in Part 2 is:", result_part2)