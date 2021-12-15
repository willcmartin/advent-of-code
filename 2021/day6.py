from collections import Counter, defaultdict

# referenced(ended up copying): https://github.com/jonathanpaulson/AdventOfCode/blob/master/2021/6.py

def read_file(filename):
    inputs = []
    with open(filename) as f:
        inputs = list(map(int, [line.strip().split(",") for line in f if line.strip()][0]))
    return inputs


def test():
    inputs_test = read_file("inputs/day6_test.txt")
    assert part1(inputs_test) == 5934
    assert part2(inputs_test) == 26984457539

def part1(inputs, days=80):
    dict = Counter(inputs)
    for _ in range(days):
        dict_temp = defaultdict(int)
        for k, v in dict.items():
            if k == 0:
                dict_temp[6] += v
                dict_temp[8] += v
            else:
                dict_temp[k-1] += v
        dict = dict_temp
    return sum(dict.values())


def part2(inputs):
    return part1(inputs, 256)


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day6.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
