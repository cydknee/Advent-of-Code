""" Day 1: Sonar Sweep """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [int(x) for x in file.read().splitlines()]


def scan_depths(depths, window):
    depth_increased = 0
    for first, second in zip(depths, depths[window::]):
        if second > first:
            depth_increased += 1
    return depth_increased


def part1():
    return scan_depths(read_file(), 1)


def part2():
    return scan_depths(read_file(), 3)


if __name__ == '__main__':
    print(part1())  # 1448
    print(part2())  # 1471
