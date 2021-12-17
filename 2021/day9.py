def read_file(filename):
    inputs = []
    with open(filename) as f:
        inputs = [list(map(int, line.strip())) for line in f if line.strip()]
    return inputs

def test():
    inputs_test = read_file("inputs/day9_test.txt")
    assert part1(inputs_test) == 15
    assert part2(inputs_test) == 1134

def get_adj(r, c, inputs):
    adj_list = []
    row_mod = [-1, 0, 1, 0]
    col_mod = [0, -1, 0, 1]
    for r_mod, c_mod in zip(row_mod, col_mod):
        r_new = r + r_mod
        c_new = c + c_mod
        if 0<=r_new<len(inputs) and 0<=c_new<len(inputs[0]):
            adj_list.append([r_new, c_new])
    return adj_list

def part1(inputs):
    tot_risk = 0
    for r in range(len(inputs)):
        for c in range(len(inputs[0])):
            if all(inputs[r][c] < inputs[r_new][c_new] for r_new, c_new in get_adj(r, c, inputs)):
                tot_risk += (inputs[r][c] + 1)
    return tot_risk

def part2(inputs):
    # code could be cleaned up quite a bit here
    visited = []
    all_basins = []
    for r in range(len(inputs)):
        for c in range(len(inputs[0])):
            if [r, c] in visited or inputs[r][c] == 9:
                continue
            basin_size = 0
            adj_all = [[r, c]]
            while adj_all:
                r_this = adj_all[0][0]
                c_this = adj_all[0][1]
                if [r_this, c_this] in visited:
                    del adj_all[0]
                    continue
                visited.append([r_this, c_this])
                basin_size += 1
                del adj_all[0]
                for r_new, c_new in get_adj(r_this, c_this, inputs):
                    if [r_new, c_new] in visited or inputs[r_new][c_new] == 9:
                        continue
                    adj_all.append([r_new, c_new])
            all_basins.append(basin_size)

    all_basins.sort()
    return all_basins[-1]*all_basins[-2]*all_basins[-3]


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day9.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
