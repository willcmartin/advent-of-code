# Day 1

def read_file(filename):
    with open(filename) as f:
        return [int(line.strip()) for line in f if line.strip()]

def test():
    inputs_test = [1721, 979, 366, 299, 675, 1456]
    assert part1(inputs_test) == 514579
    assert part2(inputs_test) == 241861950

def part1(inputs):
    for i in inputs:
        if (2020 - i) in inputs:
            return i * (2020 - i)

def part2(inputs):
    for i in range(len(inputs)):
        for j in range(len(inputs)):
            for k in range(len(inputs)):
                if i != j != k:
                    if (inputs[i] + inputs[j] + inputs[k] == 2020):
                        return inputs[i] * inputs[j] * inputs[k]

if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day1.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
