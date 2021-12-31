from collections import Counter
import copy

def read_file(filename):
    inputs = []
    with open(filename) as f:
        inputs = [line.strip().split(',') for line in f if line.strip()]
    return inputs

def test():
    inputs_test = read_file("inputs/day13_test.txt")
    assert part1(inputs_test) == 17
    assert part2(inputs_test) == None

def split_inputs(inputs):
    inputs = copy.deepcopy(inputs)
    instructions = []
    for line in inputs:
        line_str = line[0]
        if line_str.startswith("fold"):
            instructions.append(line_str.split()[-1].split("="))

    del inputs[-len(instructions):]
    inputs = [[int(x), int(y)] for x, y in inputs]

    return inputs, instructions

def part1(inputs):
    inputs, instructions = split_inputs(inputs)

    axis, val = instructions[0]
    for dot in inputs:
        if axis == "x":
            if int(val) < dot[0]:
                dot[0] -= (dot[0] - int(val))*2
        if axis == "y":
            if int(val) < dot[1]:
                dot[1] -= (dot[1] - int(val))*2

    return len([dot for i, dot in enumerate(inputs) if dot not in inputs[:i]])

def part2(inputs):
    inputs, instructions = split_inputs(inputs)

    for instruction in instructions:
        axis, val = instruction
        for dot in inputs:
            if axis == "x":
                if int(val) < dot[0]:
                    dot[0] -= (dot[0] - int(val))*2
            if axis == "y":
                if int(val) < dot[1]:
                    dot[1] -= (dot[1] - int(val))*2

    unique_dots = [dot for i, dot in enumerate(inputs) if dot not in inputs[:i]]
    unique_dots.sort()

    for c in range(min([y for x,y in unique_dots]), max([y for x,y in unique_dots])+1):
        for r in range(min([x for x,y in unique_dots]), max([x for x,y in unique_dots])+1):
            if [r, c] in unique_dots:
                print("x", end='')
            else:
                print(" ", end='')
        print()

    return None


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day13.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
