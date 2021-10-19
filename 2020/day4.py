# Day 3
import re

def read_file(filename):
    inputs = []
    person_input = {}
    with open(filename) as f:
        for line in f.readlines():
            if line == "\n":
                inputs.append(person_input)
                person_input = {}
            else:
                line_split = re.split("\s|:", line.strip())
                for i in range(0, len(line_split), 2):
                    person_input[line_split[i]] = line_split[i+1]
    inputs.append(person_input)
    return inputs

def test():
    inputs_test = read_file("inputs/day4_test.txt")
    val_inputs = [val for val in inputs_test if({"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} <= val.keys())]
    assert part1(val_inputs) == 2
    # assert part2(inputs_test) == 336

def part1(inputs):
    return len(inputs)

def part2(inputs):
    cnt = 0
    # i didn't want to rewrite it all: https://github.com/Akumatic/Advent-of-Code/blob/master/2020/04/code.py#L14
    re_patterns = {
        "byr": "19[2-9][0-9]|200[0-2]",
        "iyr": "20(1[0-9]|20)",
        "eyr": "20(2[0-9]|30)",
        "hgt": "1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in",
        "hcl": "#[0-9a-f]{6}",
        "ecl": "amb|blu|brn|gry|grn|hzl|oth",
        "pid": "[0-9]{9}",
        "cid": ".*"
    }
    for person_input in inputs:
        if all(re.fullmatch(re_patterns[v], person_input[v]) for v in person_input):
            cnt += 1
    return cnt


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day4.txt")
    val_inputs = [val for val in inputs if({"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} <= val.keys())]
    print("Part 1: {}".format(part1(val_inputs)))
    print("Part 2: {}".format(part2(val_inputs)))
