import heapq

# Used for reference: https://github.com/jonathanpaulson/AdventOfCode/blob/master/2021/15.py

def read_file(filename):
    inputs = []
    with open(filename) as f:
        inputs = [[int(char) for char in line.strip()] for line in f if line.strip()]
    return inputs

def test():
    inputs_test = read_file("inputs/day15_test.txt")
    assert part1(inputs_test) == 40
    assert part2(inputs_test) == 315

def part1(inputs, multiplier=1):
    Q = [(0, 0, 0)] # heap queue: dist, row, col
    d_row = [0, -1, 0, 1]
    d_col = [1, 0, -1, 0]

    tot_row = len(inputs)
    tot_col = len(inputs[0])

    visited = [[None for _ in range(tot_col*multiplier)] for _ in range(tot_row*multiplier)]
    
    # Dijkstra's Algorithm
    while Q:
        curr = heapq.heappop(Q)
        for i in range(4):
            next_row = curr[1] + d_row[i]
            next_col = curr[2] + d_col[i]
            if next_row >= 0 and next_row < tot_row*multiplier and next_col >= 0 and next_col < tot_col*multiplier:\

                prev_val = inputs[next_row%tot_row][next_col%tot_col]
                prev_val += next_row//tot_row + next_col//tot_col
                while prev_val > 9:
                    prev_val -= 9

                next_dist = curr[0] + prev_val

                if visited[next_row][next_col] == None or visited[next_row][next_col] > next_dist:
                    next = (next_dist, next_row, next_col)
                    heapq.heappush(Q, next)
                    visited[next_row][next_col] = next_dist

        if Q[0][1] == tot_row*multiplier-1 and Q[0][2] == tot_col*multiplier-1:
            break

    return Q[0][0]

def part2(inputs):
    return part1(inputs, multiplier=5)


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day15.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
