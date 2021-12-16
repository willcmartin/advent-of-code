def read_file(filename):
    inputs = []
    with open(filename) as f:
        inputs = [list(map(int, line.strip())) for line in f if line.strip()]
    return inputs

def test():
    inputs_test = read_file("inputs/day9_test.txt")
    assert part1(inputs_test) == 15
    assert part2(inputs_test) == 1134

def part1(inputs):
    def get_adj(r, c):
        adj_list = []
        row_mod = [-1, 0, 1, 0]
        col_mod = [0, -1, 0, 1]
        for r_mod, c_mod in zip(row_mod, col_mod):
            r_new = r + r_mod
            c_new = c + c_mod
            if 0<=r_new<len(inputs) and 0<=c_new<len(inputs[0]):
                adj_list.append(inputs[r_new][c_new])
        return adj_list

    tot_risk = 0

    for r in range(len(inputs)):
        for c in range(len(inputs[0])):
            if all(inputs[r][c] < adj for adj in get_adj(r, c)):
                tot_risk += (inputs[r][c] + 1)

    return tot_risk

def part2(inputs):
    return None


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day9.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
