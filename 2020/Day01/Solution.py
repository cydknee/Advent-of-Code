""" Day 1: Report Repair """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [int(x) for x in file.read().splitlines()]


def scan_for_two_numbers(report):
    for line in report:
        entry = 2020 - line
        if entry in report:
            return entry * line


def scan_for_three_numbers(report):
    for first_entry in report:
        for second_entry in report:
            entry = 2020 - (first_entry + second_entry)
            if entry in report:
                return entry * first_entry * second_entry


def part1():
    return scan_for_two_numbers(read_file())


def part2():
    return scan_for_three_numbers(read_file())


if __name__ == '__main__':
    print(part1())  # 1006875
    print(part2())  # 165026160