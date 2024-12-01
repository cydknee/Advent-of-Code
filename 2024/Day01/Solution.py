""" AoC 2024 Day 1: Historian Hysteria """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        locations = list(zip(*[[int(y) for y in x.split("   ")] for x in file.read().splitlines()]))
        return list(locations[0]), list(locations[1])


def part1(location_1, location_2):
    location_1.sort(), location_2.sort()
    return sum(abs(location[1] - location[0]) for location in list(zip(location_1, location_2)))


def part2(location_1, location_2):
    return sum(location * location_2.count(location) for location in location_1)


if __name__ == '__main__':
    list_1, list_2 = read_file()
    print(part1(list_1, list_2))  # 2164381
    print(part2(list_1, list_2))  # 20719933