""" AoC 2024 Day 6: Guard Gallivant """

FILE_NAME = "../../testInput.txt"
DIRECTIONS = ['<', '^', '>', 'V']

def read_file():
    with open(FILE_NAME, "r") as file:
        return [x for x in file.read().splitlines()]


def get_guard_position(data):
    for row_index, rows in enumerate(data):
        for col_index, col in enumerate(rows):
            if col in DIRECTIONS:
                return row_index, col_index, col


def part1(area_map):
    g_row, g_col, direction = get_guard_position(area_map)
    print(g_row, g_col, direction)
    while True:
        try:
           print()
        except IndexError:
            print("Guard walked off map")
            break
    return None


def part2(reports):
    return None


if __name__ == '__main__':
    print(part1(read_file()))  #
    print(part2(read_file()))  #