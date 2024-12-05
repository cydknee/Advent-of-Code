""" AoC 2024 Day 3: Mull It Over """
import re

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return file.read()


def part1(program):
    return sum([int(x[0]) * int(x[1]) for x in [mul[4:-1].split(',') for mul in re.findall(r'mul\([\d]+,[\d]+\)', program)]])


def part2(program):
    total = 0
    perform_mul = True
    for mul in re.findall(r'do\(\)|don\'t\(\)|mul\([\d]+,[\d]+\)', program):
        if mul == 'do()':
            perform_mul = True
        elif mul == "don't()":
            perform_mul = False
        else:
            if perform_mul:
                total += [x * y for x, y in [map(int, mul[4:-1].split(','))]][0]
    return total


if __name__ == '__main__':
    print(part1(read_file()))  # 185797128
    print(part2(read_file()))  # 89798695
