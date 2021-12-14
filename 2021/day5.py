import numpy as np

def read_file(filename):
    inputs = []
    with open(filename) as f:
        for line in f:
            inputs.append(list(map(int, line.strip().replace(" -> ", ",").split(","))))
    return inputs


def test():
    inputs_test = read_file("inputs/day5_test.txt")
    assert part1(inputs_test) == 5
    assert part2(inputs_test) == 12

def part1(inputs):
    inputs = [i for i in inputs if (i[0]==i[2] or i[1]==i[3])]

    coors_dict = {}
    for i in inputs:
        for x in range(min(i[0], i[2]), max(i[0], i[2])+1):
            for y in range(min(i[1], i[3]), max(i[1], i[3])+1):
                coor = str([x,y])
                if coor in coors_dict:
                    coors_dict[coor] += 1
                else:
                    coors_dict[coor] = 1

    return sum([coors_dict[c] > 1 for c in coors_dict])

def part2(inputs):
    # notation could be cleaned up a lot
    # also very slow

    def at_45(p1, p2):
        return abs(p1[0]-p2[0]) == abs(p1[1]-p2[1])

    def at_90(p1, p2):
        return p1[0]==p2[0] or p1[1]==p2[1]

    inputs = [i for i in inputs if (at_90([i[0], i[1]], [i[2], i[3]]) or at_45([i[0], i[1]], [i[2], i[3]]))]

    coors_dict = {}
    for i in inputs:
        for x in range(min(i[0], i[2]), max(i[0], i[2])+1):
            for y in range(min(i[1], i[3]), max(i[1], i[3])+1):
                if (at_45([i[0], i[1]], [i[2], i[3]]) and at_45([i[0], i[1]], [x,y])) or (at_90([i[0], i[1]], [i[2], i[3]]) and at_90([i[0], i[1]], [x,y])):
                    coor = str([x,y])
                    if coor in coors_dict:
                        coors_dict[coor] += 1
                    else:
                        coors_dict[coor] = 1

    return sum([coors_dict[c] > 1 for c in coors_dict])


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day5.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
