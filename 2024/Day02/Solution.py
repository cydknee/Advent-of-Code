""" AoC 2024 Day 2: Red-Nosed Reports """

FILE_NAME = "../../Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [[int(y) for y in x.split(" ")] for x in file.read().split("\n")]


def safe(report):
    count = len([index for index in range(len(report[:-1])) if (0 < abs(report[index] - report[index + 1]) < 4)])
    return (sorted(report) == report or sorted(report, reverse=True) == report) and count == len(report) - 1


def part1(reports):
    return len([r for r in reports if safe(r)])


def part2(reports):
    safe_count = part1(reports)

    for report in [r for r in reports if not safe(r)]:
        for index in range(len(report)):
            if safe([element for i, element in enumerate(report) if i != index]):
                safe_count += 1
                break

    return safe_count


if __name__ == '__main__':
    print(part1(read_file()))
    print(part2(read_file()))