""" AoC 2024 Day 1: Historian Hysteria """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        locations = list(zip(*[[int(y) for y in x.split("   ")] for x in file.read().splitlines()]))
        return list(locations[0]), list(locations[1])


def part1():
    distance = 0
    list_1, list_2 = read_file()
    list_1.sort(), list_2.sort()
    for location in list(zip(list_1, list_2)):
        distance += abs(location[1] - location[0])
    return distance


def part2():
    similarity = 0
    list_1, list_2 = read_file()
    for location in list_1:
        similarity += location * list_2.count(location)
    return similarity


if __name__ == '__main__':
    print(part1())  # 2164381
    print(part2())  # 20719933