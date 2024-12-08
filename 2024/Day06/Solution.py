""" AoC 2024 Day 6: Guard Gallivant """

from colorama import init
from termcolor import colored


FILE_NAME = "Input.txt"
DIRECTIONS = ['<', '^', '>', 'V']


def read_file():
    with open(FILE_NAME, "r") as file:
        return [list(x) for x in file.read().splitlines()]


def get_guard_position(data):
    for row_index, rows in enumerate(data):
        for col_index, col in enumerate(rows):
            if col in DIRECTIONS:
                return row_index, col_index, DIRECTIONS.index(col)


def print_map(data):
    init()
    for row_index, rows in enumerate(data):
        for col_index, col in enumerate(rows):
            match col:
                case '.':
                    print(col, end=' ')
                case "#":
                    print(colored(col, 'green'), end=' ')
                case '<', '^', '>', 'V':
                    print(colored(col, 'red'), end=' ')
                case 'X':
                    print(colored(col, 'yellow'), end=' ')
        print()


def count_xs(data):
    t = [[len(col) for col in rows if col == 'X'] for rows in data]
    print(t)

    count = 0
    for row_index, rows in enumerate(data):
        for col_index, col in enumerate(rows):
            if col == 'X':
                count += 1
    return count


def part1(area_map):
    row, col, direction = get_guard_position(area_map)
    while True:
        next_row, next_col = row, col
        match DIRECTIONS[direction]:
            case "^":
                next_row -= 1
            case ">":
                next_col += 1
            case "V":
                next_row += 1
            case "<":
                next_col -= 1

        if area_map[next_row][next_col] == "#":
            direction = (direction + 1) % len(DIRECTIONS)
        else:
            area_map[row][col] = "X"
            row, col = next_row, next_col
        area_map[row][col] = DIRECTIONS[direction]

        if not (0 < row < len(area_map[0])) or not (0 < col < len(area_map)):
            break
    return count_xs(area_map) + 1


def part2(reports):
    return None


if __name__ == '__main__':
    print(part1(read_file()))  # 4967
    print(part2(read_file()))  #
