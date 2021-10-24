# Day 8
import copy

def read_file(filename):
    inputs = []
    with open(filename) as f:
        for line in f.read().strip().split("\n"):
            inputs.append(line.split(" "))
    return inputs

def test():
    inputs_test = read_file("inputs/day8_test.txt")
    assert part1(inputs_test)[1] == 5
    assert part2(inputs_test) == 8

def part1(inputs):
    i = 0
    accumulator = 0
    instructions_visited = []
    while i not in instructions_visited:
        instructions_visited.append(i)
        op, arg = inputs[i]
        sign = arg[0]
        val = int(arg[1:])

        if op == 'acc':
            i += 1
            if sign == '+':
                accumulator += val
            else:
                accumulator -= val
        elif op == 'jmp':
            if sign == '+':
                i += val
            else:
                i -= val
        elif op == 'nop':
            i += 1
        else:
            raise ValueError()

        if i >= len(inputs):
            return True, accumulator

    return False, accumulator

def part2(inputs):
    for i in range(len(inputs)):
        temp_inputs = copy.deepcopy(inputs) # slow but the best way I could find to copy list of list
        if inputs[i][0] == 'jmp':
            temp_inputs[i][0] = 'nop'
        elif inputs[i][0] == 'nop':
            temp_inputs[i][0] = 'jmp'
        else:
            continue
        results, accumulator = part1(temp_inputs)
        if results:
            return accumulator
    return -1


if __name__ == "__main__":
    inputs = read_file("inputs/day8.txt")
    print("Part 1: {}".format(part1(inputs)[1]))
    print("Part 2: {}".format(part2(inputs)))
    test()
