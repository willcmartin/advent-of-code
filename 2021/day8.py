from collections import defaultdict

"""
Part 1:
    num -> seg cnt
    1 -> 2
    4 -> 4
    7 -> 3
    8 -> 7

Part 2
    unique rule: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    0 -> 6
    1 -> 2 (unique)
    2 -> 5
    3 -> 5
    4 -> 4 (unique)
    5 -> 5
    6 -> 6
    7 -> 3 (unique)
    8 -> 7 (unique)
    9 -> 6

    diff 6, 9, 0 -> 6
    7 not in 6
    4 in 9
    0 is remaining

    diff 2, 3, 5 -> 5
    1 in 3 not in 2 and 5
    9 - 8 in 2 not 5
    5 is remaining


"""

def read_file(filename):
    inputs = []
    with open(filename) as f:
        inputs = [[num.strip().split(" ") for num in line.strip().split("|")] for line in f if line.strip()]
    return inputs

def test():
    inputs_test = read_file("inputs/day8_test.txt")
    assert part1(inputs_test) == 26
    assert part2(inputs_test) == 61229

def part1(inputs):
    tot = 0
    for display in inputs:
        for output in display[1]:
            if len(output) in [2, 4, 3, 7]:
                tot += 1
    return tot

def part2(inputs):
    all_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    tot_output = 0
    for display in inputs:
        # create dictionary of sorted characters associated with each number
        num_dict = defaultdict()
        for pattern in display[0]:
            # 1
            if len(pattern) == 2:
                num_dict[1] = sorted(list(pattern))
            # 7
            elif len(pattern) == 3:
                num_dict[7] = sorted(list(pattern))
            # 4
            elif len(pattern) == 4:
                num_dict[4] = sorted(list(pattern))
            # 8
            elif len(pattern) == 7:
                num_dict[8] = sorted(list(pattern))

        for pattern in display[0]:
            # 6, 9, or 0
            if len(pattern) == 6:
                # 9
                if all(elem in sorted(list(pattern)) for elem in num_dict[4]):
                    num_dict[9] = sorted(list(pattern))
                # 6
                elif ''.join(set(all_char) - set(list(pattern))) in num_dict[7]:
                    num_dict[6] = sorted(list(pattern))
                # 0
                else:
                    num_dict[0] = sorted(list(pattern))

        for pattern in display[0]:
            # 2, 3, or 5
            if len(pattern) == 5:
                # 3
                if all(elem in sorted(list(pattern)) for elem in num_dict[1]):
                    num_dict[3] = sorted(list(pattern))
                # 2
                elif ''.join(set(num_dict[8]) - set(num_dict[9])) in pattern:
                    num_dict[2] = sorted(list(pattern))
                # 5
                else:
                    num_dict[5] = sorted(list(pattern))

        # find numbers from output
        output = ""
        for pattern in display[1]:
            for key, value in num_dict.items():
                 if sorted(list(pattern)) == value:
                     output += str(key)
        tot_output += int(output)
    return tot_output


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day8.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
