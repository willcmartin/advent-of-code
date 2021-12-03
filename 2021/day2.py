def read_file(filename):
    with open(filename) as f:
        return [line.strip().split(' ') for line in f]

def test():
    inputs_test = read_file("inputs/day2_test.txt")
    assert part1(inputs_test) == 150
    assert part2(inputs_test) == 900

def part1(inputs):
    h = d = 0
    for i, val in inputs:
        val = int(val)
        if i == 'forward':
            h += val
        elif i == 'down':
            d += val
        elif i == 'up':
            d -= val
        else:
            raise ValueError
    return h * d

def part2(inputs):
    h = d = a = 0
    for i, val in inputs:
        val = int(val)
        if i == 'forward':
            h += val
            d += a * val
        elif i == 'down':
            a += val
        elif i == 'up':
            a -= val
        else:
            raise ValueError
    return h * d


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day2.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
