import copy

def read_file(filename):
    inputs = []
    with open(filename) as f:
        inputs = [list(map(int, line.strip())) for line in f if line.strip()]
    return inputs

def test():
    inputs_test = read_file("inputs/day11_test.txt")
    assert part1(inputs_test) == 1656
    assert part2(inputs_test) == 195

def get_adj(r, c, inputs):
    adj_list = []
    row_mod = [-1, 0, 1, 0, 1, -1, 1, -1]
    col_mod = [0, -1, 0, 1, 1, -1, -1, 1]
    for r_mod, c_mod in zip(row_mod, col_mod):
        r_new = r + r_mod
        c_new = c + c_mod
        if 0<=r_new<len(inputs) and 0<=c_new<len(inputs[0]):
            adj_list.append([r_new, c_new])
    return adj_list

def update_adj(r, c, inputs, flashed):
    for r_adj, c_adj in get_adj(r, c, inputs):
        if inputs[r_adj][c_adj] != 9 and [r_adj, c_adj] not in flashed:
            inputs[r_adj][c_adj] += 1
        elif [r_adj, c_adj] not in flashed:
            inputs[r_adj][c_adj] = 0
            flashed.append([r_adj, c_adj])
            update_adj(r_adj, c_adj, inputs, flashed)
    return

def part1(inputs):
    # repeat for 100 steps:
    # increment all values by 1 (wrap 9 to 0)
    # add 1 to any value adjacent to a 0 if not a zero
    # count 0s

    inputs = copy.deepcopy(inputs)
    
    tot_flashes = 0
    for _ in range(100):
        flashed = []
        for r in range(len(inputs)):
            for c in range(len(inputs[0])):
                if inputs[r][c] != 9 and [r, c] not in flashed:
                    inputs[r][c] += 1
                elif [r, c] not in flashed:
                    inputs[r][c] = 0
                    flashed.append([r, c])
                    update_adj(r, c, inputs, flashed)
        tot_flashes += len(flashed)

    return tot_flashes

def part2(inputs):
    # almost all repeated code from part 1
    inputs = copy.deepcopy(inputs)

    for i in range(100000):
        flashed = []
        for r in range(len(inputs)):
            for c in range(len(inputs[0])):
                if inputs[r][c] != 9 and [r, c] not in flashed:
                    inputs[r][c] += 1
                elif [r, c] not in flashed:
                    inputs[r][c] = 0
                    flashed.append([r, c])
                    update_adj(r, c, inputs, flashed)

        if all(all(v==0 for v in value) for value in inputs):
            return i+1


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day11.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
