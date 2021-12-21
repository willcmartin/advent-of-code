from collections import deque

def read_file(filename):
    inputs = []
    with open(filename) as f:
        inputs = [list(line.strip()) for line in f if line.strip()]
    print(inputs)
    return inputs

def test():
    inputs_test = read_file("inputs/day11_test.txt")
    assert part1(inputs_test) == None
    assert part2(inputs_test) == None

def part1(inputs):
    return None

def part2(inputs):
    return None


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day11.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
