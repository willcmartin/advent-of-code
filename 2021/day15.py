import heapq

def read_file(filename):
    inputs = []
    with open(filename) as f:
        inputs = [[int(char) for char in line.strip()] for line in f if line.strip()]
    return inputs

def test():
    inputs_test = read_file("inputs/day15_test.txt")
    assert part1(inputs_test) == 40
    assert part2(inputs_test) == None

def part1(inputs):
    Q = [(0, 0, 0)] # heap queue: dist, row, col
    d_row = [0, -1, 0, 1]
    d_col = [1, 0, -1, 0]
    visited = []

    tot_row = len(inputs)
    tot_col = len(inputs[0])

    while Q:
        curr = heapq.heappop(Q)
        for i in range(4):
            next_row = curr[1] + d_row[i]
            next_col = curr[2] + d_col[i]
            if next_row >= 0 and next_row < tot_row and next_col >= 0 and next_col < tot_col and [next_row, next_col] not in visited:
                visited.append([next_row, next_col])
                next_dist = curr[0] + inputs[next_row][next_col]
                next = (next_dist, next_row, next_col)

                heapq.heappush(Q, next)

        if Q[0][1] == tot_row-1 and Q[0][2] == tot_col-1:
            break

    return Q[0][0]

def part2(inputs):
    return None


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day15.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
