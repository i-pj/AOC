def part1():
    open_bracket = 0
    close_bracket = 0
    with open("input.txt") as f:
        for line in f:
            for char in line:
                if char == "(":
                    open_bracket += 1
                elif char == ")":
                    close_bracket += 1
    print(open_bracket - close_bracket)

def part2():
    floor = 0
    with open("input.txt") as f:
        for line in f:
            for i, char in enumerate(line): 
                if char == "(":
                    floor += 1
                elif char == ")":
                    floor -= 1
                if floor == -1:
                    print(i+1)
                    break
                
part1()
part2()
