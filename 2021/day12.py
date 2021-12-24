from collections import defaultdict

def read_file(filename):
    inputs = []
    with open(filename) as f:
        inputs = [line.strip().split('-') for line in f if line.strip()]
    return inputs

def test():
    inputs_test = read_file("inputs/day12_test.txt")
    assert part1(inputs_test) == 226
    assert part2(inputs_test) == 3509

def part1(inputs):
    adj_list = defaultdict(list)
    for edge in inputs:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    visited = []
    paths = 0

    # dfs, if visit sm node in visited then skip
    def dfs(node, visited):
        nonlocal paths
        visited.append(node)
        for neighbor in adj_list[node]:
            if neighbor not in [v for v in visited if v.islower()]:
                if neighbor == 'end':
                    paths += 1
                else:
                    dfs(neighbor, visited)
                    del visited[-1]

    dfs('start', visited)

    return paths

def part2(inputs):
    return None


if __name__ == "__main__":
    test()

    inputs = read_file("inputs/day12.txt")
    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))
