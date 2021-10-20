# Day 5

def read_file(filename):
    with open(filename) as f:
        inputs = [int(line.replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0"), 2) for line in f.readlines()]
    return inputs

def test():
    pass

def part1(inputs):
    return max(inputs)

def part2(inputs):
    inputs.sort()
    for i in range(inputs[0], inputs[-1]):
        if i not in inputs and (i+1 and i-1 in inputs):
            return i


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day5.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
