import numpy as np
from pathlib import Path


def parse_instruction(line):
    direction, distance, color = line.split()
    return direction, int(distance), color.strip("(#)")


def get_vertices(instructions):
    x, y = 0, 0
    vertices = [(x, y)]
    perimeter = 0

    for direction, distance, _ in instructions:
        if direction == "R":
            x += distance
        elif direction == "L":
            x -= distance
        elif direction == "U":
            y -= distance
        elif direction == "D":
            y += distance

        vertices.append((x, y))
        perimeter += distance

    return vertices, perimeter


def shoelace_formula(vertices):
    x, y = zip(*vertices)
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


def calculate_lava_volume(instructions):
    vertices, perimeter = get_vertices(instructions)
    area = shoelace_formula(vertices)

    # Pick's theorem: A = i + b/2 - 1
    return int(area + perimeter / 2 + 1)


def main():
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as f:
        instructions = [parse_instruction(line.strip()) for line in f]

    lava_volume = calculate_lava_volume(instructions)
    print(str(lava_volume))


if __name__ == "__main__":
    main()
