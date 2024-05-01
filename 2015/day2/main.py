def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    # Part 1
    total_paper = 0
    for line in data:
        l, w, h = map(int, line.split('x'))  
        side1 = l * w
        side2 = w * h
        side3 = h * l
        total_paper += 2 * (side1 + side2 + side3) + min(side1, side2, side3)

    print(f'Part 1: {total_paper}')


    #Part 2
    total_ribbon = 0
    for line in data:
        l, w, h = map(int, line.split('x'))  
        total_ribbon += 2 * (l + w + h - max(l, w, h)) + l * w * h

    print(f'Part 2: {total_ribbon}')

main()