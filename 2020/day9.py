# Day 9
from itertools import combinations

def read_file(filename):
    inputs = []
    with open(filename) as f:
        for line in f.read().strip().split("\n"):
            inputs.append(int(line.strip()))
    return inputs

def test():
    # inputs_test = read_file("inputs/day9_test.txt")
    # assert part1(inputs_test) == 11
    # assert part2(inputs_test) == 6
    pass

def sums(sub_inputs, n=2):
    return [sum(comb) for comb in combinations(sub_inputs, n)]

def contig(sub_inputs, n):
    return [sub_inputs[i:i+n] for i in range(len(sub_inputs)-n)]

def part1(inputs):
    for i in range(25, len(inputs)):
        num = inputs[i]
        if num in sums(inputs[i-25:i]):
            continue
        else:
            return num
    return -1

def part2(inputs):
    # could this be any slower?
    # Find ways to increase speed: start search later in the list
    for i in range(2, len(inputs)-1):
        sub_set = contig(inputs, i)
        for sub_sub_set in sub_set:
            if part1(inputs) == sum(sub_sub_set):
                return min(sub_sub_set) + max(sub_sub_set)
    return -1


if __name__ == "__main__":
    inputs = read_file("inputs/day9.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
    test()
