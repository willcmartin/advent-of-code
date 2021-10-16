# Day 2

def read_file(filename):
    inputs = []
    with open(filename) as f:
        for line in f.readlines():
            txt = line.rstrip().split()
            txt[0] = txt[0].split('-')
            txt[1] = txt[1][:1]
            inputs.append(txt)
    return inputs

def test():
    inputs_test = [[['1', '3'], 'a', 'abcde'], [['1', '3'], 'b', 'cdefg'],
        [['2', '9'], 'c', 'ccccccccc']]
    assert part1(inputs_test) == 2
    assert part2(inputs_test) == 1

def part1(inputs):
    counter = 0
    for p in inputs:
        min = int(p[0][0])
        max = int(p[0][1])
        if p[2].count(p[1]) >= min and p[2].count(p[1]) <= max:
            counter += 1
    return counter

def part2(inputs):
    counter = 0
    for p in inputs:
        pos1 = int(p[0][0])
        pos2 = int(p[0][1])
        if (p[2][pos1-1] == p[1]) ^ (p[2][pos2-1] == p[1]):
            counter += 1
    return counter


if __name__ == "__main__":
    test()
    
    inputs = read_file("inputs/day2.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
