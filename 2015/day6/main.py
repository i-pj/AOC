# Day 6: Probably a Fire Hazard ---

# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

# For example:

# turn on 0,0 through 999,999 would turn on (or leave on) every light.
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
# After following the instructions, how many lights are lit?

    
# def main():
#     with open('input.txt', 'r') as f:
#         instructions = f.readlines()

#     lights = [[0 for _ in range(1000)] for _ in range(1000)]

#     for instruction in instructions:
#         instruction = instruction.strip().split(' ')
#         if instruction[0] == 'toggle':
#             x1, y1 = map(int, instruction[1].split(','))
#             x2, y2 = map(int, instruction[3].split(','))
#             for i in range(x1, x2 + 1):
#                 for j in range(y1, y2 + 1):
#                     lights[i][j] = 1 - lights[i][j]
#         elif instruction[1] == 'on':
#             x1, y1 = map(int, instruction[2].split(','))
#             x2, y2 = map(int, instruction[4].split(','))
#             for i in range(x1, x2 + 1):
#                 for j in range(y1, y2 + 1):
#                     lights[i][j] = 1
#         elif instruction[1] == 'off':
#             x1, y1 = map(int, instruction[2].split(','))
#             x2, y2 = map(int, instruction[4].split(','))
#             for i in range(x1, x2 + 1):
#                 for j in range(y1, y2 + 1):
#                     lights[i][j] = 0

#     print(sum([sum(row) for row in lights]))

# if __name__ == '__main__':
#     main()
from re import findall

def calculate_total_brightness(input_string):
    light_actions = {
        'toggle': lambda brightness: brightness + 2,
        'turn on': lambda brightness: brightness + 1,
        'turn off': lambda brightness: max(brightness - 1, 0)
    }
    light_grid = [[0 for _ in range(1000)] for _ in range(1000)]
    instructions = findall("(toggle|turn on|turn off)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)", input_string)
    for action, x1, y1, x2, y2 in instructions:
        coordinates = [(x, y) for x in range(int(x1), int(x2) + 1) for y in range(int(y1), int(y2) + 1)]
        for x, y in coordinates:
            light_grid[x][y] = light_actions[action](light_grid[x][y])
    return sum(val for sublist in light_grid for val in sublist)

def main():

    with open('input.txt', 'r') as f:
        input_string = f.read()

    print(calculate_total_brightness(input_string))

if __name__ == '__main__':
    main()
    