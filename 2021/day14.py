from collections import Counter
import math

def read_file(filename):
    inputs = []
    with open(filename) as f:
        inputs = [line.strip().split(' -> ') for line in f if line.strip()]
    return inputs[0][0], inputs[1:]

def test():
    inputs_test = read_file("inputs/day14_test.txt")
    assert part1(inputs_test) == 1588
    assert part2(inputs_test) == 2188189693529

def part1(inputs, steps=10):
    template, rules = inputs

    pair_counter = Counter()
    for i in range(len(template)-1):
        pair_counter[template[i]+template[i+1]] += 1

    for _ in range(steps):
        pair_counter_new = Counter()
        for pair in pair_counter:
            rules_pairs = [r[0] for r in rules]
            if pair in rules_pairs:
                pair_counter_new[pair[0]+rules[rules_pairs.index(pair)][1]] += pair_counter[pair]
                pair_counter_new[rules[rules_pairs.index(pair)][1]+pair[1]] += pair_counter[pair]
            else:
                pair_counter_new[pair] += pair_counter[pair]
        pair_counter = pair_counter_new

    letter_counter = Counter()
    for pair in pair_counter:
        letter_counter[pair[0]] += pair_counter[pair]
        letter_counter[pair[1]] += pair_counter[pair]

    max_cnt = math.ceil(max(letter_counter.values())/2)
    min_cnt = math.ceil(min(letter_counter.values())/2)

    return max_cnt-min_cnt

def part2(inputs):
    return part1(inputs, steps=40)


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day14.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
