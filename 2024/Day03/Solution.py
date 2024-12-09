""" AoC 2024 Day 3: Mull It Over """
import re

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return file.read()


def solution(expression):
    total = 0
    perform_mul = True
    for mul in re.findall(expression, read_file()):
        if mul == 'do()':
            perform_mul = True
        elif mul == "don't()":
            perform_mul = False
        else:
            if perform_mul:
                total += [x * y for x, y in [map(int, mul[4:-1].split(','))]][0]
    return total


def part1():
    return solution(r'mul\([\d]+,[\d]+\)')


def part2():
    return solution(r'do\(\)|don\'t\(\)|mul\([\d]+,[\d]+\)')


if __name__ == '__main__':
    print(part1())  # 185797128
    print(part2())  # 89798695
