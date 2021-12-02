# Day 1

def read_file(filename):
    with open(filename) as f:
        return [int(line.strip()) for line in f if line.strip()]

def test():
    inputs_test = read_file("inputs/day1_test.txt")
    assert part1(inputs_test) == 7
    assert part2(inputs_test) == 5

def part1(inputs):
    temp = inputs[0]
    counter = 0
    for num in inputs[1:]:
        if num > temp:
            counter += 1
        temp = num
    return counter

def part2(inputs):
    counter = 0
    temp_window_sum = 1000000
    for i in range(len(inputs[:-2])):
        window_sum = sum(inputs[i:i+3])
        if window_sum > temp_window_sum:
            counter += 1
        temp_window_sum = window_sum
    return counter


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day1.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
