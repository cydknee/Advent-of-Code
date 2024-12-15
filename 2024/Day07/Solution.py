""" AoC 2024 Day 7: Bridge Repair """

FILE_NAME = "testInput.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [[[int(z) for z in y.split(" ")] for y in x.split(": ")] for x in file.read().splitlines()]


def part1(report):
    for line in report:
        target = line[0][0]
        print(target, end=" ")
        for num in line[1]:
            print(num, end=" ")

        print()
    return None


def part2(reports):
    return None


if __name__ == '__main__':
    print(part1(read_file()))  #
    print(part2(read_file()))  #
