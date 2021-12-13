import numpy as np

def read_file(filename):
    with open(filename) as f:
        inputs = [line.strip() for line in f if line.strip()]
    numbers = np.asarray(inputs[0].split(","), dtype=int)
    boards = np.asarray([[num.split() for num in (inputs[i:i+5])] for i in range(1, len(inputs)-1, 5)], dtype=int)
    return (numbers, boards)


def test():
    inputs_test = read_file("inputs/day4_test.txt")
    assert part1(inputs_test) == 4512
    assert part2(inputs_test) == 1924

def part1(inputs):
    numbers, boards = inputs
    boards = np.copy(boards)
    for n in numbers:
        for b in boards:
            b[b == n] = -1
            if any((b == -1).all(axis=0)) or any((b == -1).all(axis=1)):
                b[b == -1] = 0
                return np.sum(b) * n

def part2(inputs):
    numbers, boards = inputs
    boards = np.copy(boards)
    boards_won = []
    for n in numbers:
        for i, b in enumerate(boards):
            if i not in boards_won:
                b[b == n] = -1
                if any((b == -1).all(axis=0)) or any((b == -1).all(axis=1)):
                    if len(boards_won) == np.shape(boards)[0]-1:
                        b[b == -1] = 0
                        return np.sum(b) * n
                    else:
                        boards_won.append(i)


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day4.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
