# Day 2

def read_file(filename):
    inputs = []
    with open(filename) as f:
        for line in f.readlines():
            inputs.append(list(line.strip()))
    return inputs

def test():
    inputs_test = read_file("inputs/day3_test.txt")
    assert part1(inputs_test) == 7
    assert part2(inputs_test) == 336

def part1(inputs):
    cnt = row = col = 0
    while row < len(inputs):
        if inputs[row][col] == "#":
            cnt += 1
        row += 1
        col += 3
        if col >= len(inputs[0]):
            col -= len(inputs[0])
    return cnt

def part2(inputs):
    row_mult = [1, 1, 1, 1, 2]
    col_mult = [1, 3, 5, 7, 1]
    tot_cnt = 1

    for r_mult, c_mult in zip(row_mult, col_mult):
        cnt = row = col = 0
        while row < len(inputs):
            if inputs[row][col] == "#":
                cnt += 1
            row += r_mult
            col += c_mult
            if col >= len(inputs[0]):
                col -= len(inputs[0])
        tot_cnt *= cnt
    return tot_cnt


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day3.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
