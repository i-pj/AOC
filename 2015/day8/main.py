import re
from typing import List

def part1(data: List[str]) -> int:
    sums = 0
    for code in data:
        original_len = len(code)
        decoded_len = len(eval(code))
        sums += original_len - decoded_len
    return sums

def part2(data: List[str]) -> int:
    sums = 0
    for code in data:
        original_len = len(code)
        encoded_string = re.sub(r'([\\"])', r'\\\1', code)
        encoded_string = '"' + encoded_string + '"'
        encoded_len = len(encoded_string)
        sums += encoded_len - original_len
    return sums

def main():
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
        print("Part 1:", part1(data))
        print("Part 2:", part2(data))

if __name__ == "__main__":
    main()