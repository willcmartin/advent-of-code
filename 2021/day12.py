import copy

def read_file(filename):
    inputs = []
    with open(filename) as f:
        inputs = [line.strip().split('-') for line in f if line.strip()]
    print(inputs)
    return inputs

def test():
    inputs_test = read_file("inputs/day12_test.txt")
    assert part1(inputs_test) == 226
    assert part2(inputs_test) == None

def part1(inputs):
    return None

def part2(inputs):
    return None


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day12.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
