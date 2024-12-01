""" Day 3: Toboggan Trajectory """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return file.read().splitlines()


def move_down_slope(tree_map, right, down):
    position, tree_count = 0, 0
    for line in tree_map[down::down]:
        position = ((position + right) % len(tree_map[0]))
        if line[position] == "#":
            tree_count += 1
    return tree_count


def part1():
    return move_down_slope(read_file(), 3, 1)


def part2():
    tree_count = 1
    for right, down in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
        tree_count *= move_down_slope(read_file(), right, down)
    return tree_count


if __name__ == '__main__':
    print(part1())  # 250
    print(part2())  # 1592662500
