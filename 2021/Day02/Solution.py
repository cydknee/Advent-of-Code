""" Day 2: Dive! """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [[y for y in x.split()] for x in file.read().splitlines()]


def calculate_position(course):
    horizontal, depth, aim = 0, 0, 0
    for instruction, amount in course:
        if instruction == "forward":
            horizontal += int(amount)
            depth += aim * int(amount)
        elif instruction == "down":
            aim += int(amount)
        else:
            aim -= int(amount)
    return (horizontal * aim), (horizontal * depth)


def part1():
    return calculate_position(read_file())[0]


def part2():
    return calculate_position(read_file())[1]


if __name__ == '__main__':
    print(part1())  # 1893605
    print(part2())  # 2120734350
