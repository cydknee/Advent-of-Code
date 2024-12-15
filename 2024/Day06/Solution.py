""" AoC 2024 Day 6: Guard Gallivant """

FILE_NAME = "Input.txt"
DIRECTIONS = ['<', '^', '>', 'V']
MOVEMENT = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def read_file():
    with open(FILE_NAME, "r") as file:
        return [list(x) for x in file.read().splitlines()]


def find_guard(grid):
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if grid[row_index][col_index] in DIRECTIONS:
                return row_index, col_index, DIRECTIONS.index(grid[row_index][col_index])


def guards_route(grid, row, col, direction):
    direction_row, direction_column = MOVEMENT[direction]
    part_1_positions, part_2_positions = set(), set()

    while True:
        part_1_positions.add((row, col))
        part_2_positions.add((row, col, direction_row, direction_column))

        next_row = row + direction_row
        next_col = col + direction_column

        if next_row < 0 or next_row >= len(grid) or next_col < 0 or next_col >= len(grid[0]):
            return part_1_positions
        elif grid[next_row][next_col] == "#":
            direction = (direction + 1) % len(DIRECTIONS)
            direction_row, direction_column = MOVEMENT[direction]
        else:
            row += direction_row
            col += direction_column

        if (row, col, direction_row, direction_column) in part_2_positions:
            return True


def part1(grid):
    guard_row, guard_col, guard_direction = find_guard(grid)
    return guards_route(grid, guard_row, guard_col, guard_direction)


def part2(grid, guard_route):
    count = 0
    guard_row, guard_col, guard_direction = find_guard(grid)

    for (row_index, col_index) in guard_route:
        if grid[row_index][col_index] != ".":
            continue
        grid[row_index][col_index] = "#"
        if guards_route(grid, guard_row, guard_col, guard_direction) == True:
            count += 1
        grid[row_index][col_index] = "."

    return count


if __name__ == '__main__':
    grid_map = read_file()
    print(len(part1(grid_map)))  # 4967
    print(part2(grid_map, part1(grid_map)))  # 1789
