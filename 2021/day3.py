def read_file(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

def test():
    inputs_test = read_file("inputs/day3_test.txt")
    assert part1(inputs_test) == 198
    assert part2(inputs_test) == 230

def part1(inputs):
    gamma = ''
    for pos in range(len(inputs[0])):
        if sum([int(byte[pos]) for byte in inputs]) > len(inputs)/2:
            gamma += '1'
        else:
            gamma += '0'
    gamma = int(gamma, base=2)
    epsilon = 2**len(inputs[0]) - 1 - gamma
    return gamma * epsilon

def part2(inputs):
    temp_inputs_oxy = inputs
    temp_inputs_co2 = inputs
    for pos in range(len(inputs[0])):
        if len(temp_inputs_oxy) > 1:
            if sum([int(byte[pos]) for byte in temp_inputs_oxy]) >= len(temp_inputs_oxy)/2:
                temp_inputs_oxy = [i for i in temp_inputs_oxy if i[pos] == '1']
            else:
                temp_inputs_oxy = [i for i in temp_inputs_oxy if i[pos] == '0']
                
        if len(temp_inputs_co2) > 1:
            if sum([int(byte[pos]) for byte in temp_inputs_co2]) < len(temp_inputs_co2)/2:
                temp_inputs_co2 = [i for i in temp_inputs_co2 if i[pos] == '1']
            else:
                temp_inputs_co2 = [i for i in temp_inputs_co2 if i[pos] == '0']

    oxy = int(temp_inputs_oxy[0], base=2)
    co2 = int(temp_inputs_co2[0], base=2)

    return oxy * co2


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day3.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
