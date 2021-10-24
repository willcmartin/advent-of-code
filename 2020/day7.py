# Day 7

# this one is could use a lot of improvements

def read_file(filename):
    inputs = {}
    with open(filename) as f:
        for line in f.read().replace('.','').replace('contain', ',').replace('bags', '').replace('bag', '').split("\n"):
            if line:
                split_line = line.split(",")
                inner_bags = []
                for s in split_line[1:]:
                    inner_bags.append((s[1], s[3:-1]))
                inputs[split_line[0][:-2]] = inner_bags
    return inputs

def test():
    inputs_test = read_file("inputs/day7_test.txt")
    assert part1(inputs_test) == 4
    assert part2(inputs_test) == 32
    pass

def contains(inputs, outer_bag):
    if outer_bag == 'shiny gold':
        return True
    if outer_bag == ' other':
        return False
    for inner in inputs.get(outer_bag):
        if contains(inputs, inner[1]):
            return True
    return False

def part1(inputs):
    cnt = 0
    for input in inputs:
        if contains(inputs, input):
            cnt += 1
    return cnt - 1

def num_contains(inputs, outer_bag):
    tot = 0
    inner_bags = inputs.get(outer_bag)
    if inner_bags[0][1] == ' other':
        return 0
    for inner in inner_bags:
        tot += (int(inner[0]) + int(inner[0])*num_contains(inputs, inner[1]))
    return tot


def part2(inputs):
    return num_contains(inputs, 'shiny gold')


if __name__ == "__main__":
    inputs = read_file("inputs/day7.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
    test()
