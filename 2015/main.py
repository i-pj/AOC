import math

def sum_of_divisors(n):
    sum = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum += i
            if i * i!= n:
                sum += n // i
    return sum * 10

def find_house_with_at_least_presents(presents_threshold):
    house_number = 1
    while True:
        if sum_of_divisors(house_number) >= presents_threshold:
            return house_number
        house_number += 1

puzzle_input = 29000000
result = find_house_with_at_least_presents(puzzle_input)
print("The lowest house number to get at least", puzzle_input, "presents is:", result)