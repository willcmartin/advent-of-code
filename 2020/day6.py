# Day 6

def read_file(filename):
    inputs = []
    with open(filename) as f:
        for line in f.read().split("\n\n"):
            inputs.append(line.strip().split("\n"))
    return inputs

def test():
    inputs_test = read_file("inputs/day6_test.txt")
    assert part1(inputs_test) == 11
    assert part2(inputs_test) == 6

def part1(inputs):
    return sum([len(set("".join(group))) for group in inputs])

def part2(inputs):
    tot_sum = 0
    for group in inputs:
        chars = set("".join(group))
        for c in chars:
            if all(c in person for person in group):
                tot_sum += 1
    return tot_sum


if __name__ == "__main__":
    inputs = read_file("inputs/day6.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
    test()
