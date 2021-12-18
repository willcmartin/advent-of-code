from collections import deque

def read_file(filename):
    inputs = []
    with open(filename) as f:
        inputs = [list(line.strip()) for line in f if line.strip()]
    return inputs

def test():
    inputs_test = read_file("inputs/day10_test.txt")
    assert part1(inputs_test) == 26397
    assert part2(inputs_test) == 288957

def part1(inputs):
    score = 0
    brackets = {')':'(', ']':'[', '}':'{', '>':'<'}
    bracket_values = {')':3, ']':57, '}':1197, '>':25137}
    for line in inputs:
        stack = deque()
        for char in line:
            if char in brackets.values():
                stack.append(char)
            else:
                if stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    score += bracket_values[char]
                    break
    return score

def part2(inputs):
    all_scores = []
    brackets = {')':'(', ']':'[', '}':'{', '>':'<'}
    brackets_reversed = dict((y,x) for x,y in brackets.items())
    bracket_values = {')':1, ']':2, '}':3, '>':4}
    for line in inputs:
        stack = deque()
        score = 0
        for char in line:
            if char in brackets.values():
                stack.append(char)
            else:
                if stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    break
        else: # executed after the for, but only if the for terminates normally (not by a break) (http://psung.blogspot.com/2007/12/for-else-in-python.html)
            while stack:
                score = (score * 5) + bracket_values[brackets_reversed[stack.pop()]]
            all_scores.append(score)

    return sorted(all_scores)[int(len(all_scores)/2)]


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day10.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
