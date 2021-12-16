import statistics

# Part 1:
# cost = abs(x0-z)
# d(cost)/dz = -1 (x0>z) or 1 (x0<z)
# sum(d(cost)/dz) = 0
# balance (x0>z) and (x0<z)
# find median of x0's

# Part 2:
# cost = 1 + 2 + ... + abs(x0-z) = [(abs(x0-z))^2 + abs(x0-z)]/2

def read_file(filename):
    inputs = []
    with open(filename) as f:
        inputs = list(map(int, [line.strip().split(",") for line in f if line.strip()][0]))
    return inputs

def test():
    inputs_test = read_file("inputs/day7_test.txt")
    assert part1(inputs_test) == 37
    assert part2(inputs_test) == 168

def part1(inputs):
    median = int(statistics.median(inputs))
    fuel = sum([abs(pos-median) for pos in inputs])
    return fuel

def part2(inputs):
    # brute force
    best = 1e9
    for i in range(max(inputs)):
        tot_cost = 0
        for pos in inputs:
            val = abs(pos-i)
            cost = int((val*(val+1))/2)
            tot_cost += cost
        if tot_cost < best:
            best = tot_cost
    return best


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day7.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
