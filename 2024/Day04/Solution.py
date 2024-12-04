""" AoC 2024 Day 4: Ceres Search """

FILE_NAME = "Input.txt"
MAS = ['M', 'A', 'S']


def read_file():
    with open(FILE_NAME, "r") as file:
        return [list(x) for x in file.read().split("\n")]


def part1(grid):
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'X':
                if col < len(grid[0][:-3]) and \
                        [grid[row][col + 1], grid[row][col + 2], grid[row][col + 3]] == MAS:
                    count += 1
                if col > 2 and \
                        [grid[row][col - 1], grid[row][col - 2], grid[row][col - 3]] == MAS:
                    count += 1
                if row > 2 and \
                        [grid[row - 1][col], grid[row - 2][col], grid[row - 3][col]] == MAS:
                    count += 1
                if row < len(grid[:-3]) and \
                        [grid[row + 1][col], grid[row + 2][col], grid[row + 3][col]] == MAS:
                    count += 1
                if (row > 2 and col > 2) and \
                        [grid[row - 1][col - 1], grid[row - 2][col - 2], grid[row - 3][col - 3]] == MAS:
                    count += 1
                if (row > 2 and col < len(grid[0][:-3])) and \
                        [grid[row - 1][col + 1], grid[row - 2][col + 2], grid[row - 3][col + 3]] == MAS:
                    count += 1
                if (row < len(grid[:-3]) and col > 2) and \
                        [grid[row + 1][col - 1], grid[row + 2][col - 2], grid[row + 3][col - 3]] == MAS:
                    count += 1
                if (row < len(grid[:-3]) and col < len(grid[0][:-3])) \
                        and [grid[row + 1][col + 1], grid[row + 2][col + 2], grid[row + 3][col + 3]] == MAS:
                    count += 1
    return count


def part2(grid):
    count = 0
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col] == 'A':
                if ([grid[row - 1][col - 1], grid[row][col], grid[row + 1][col + 1]] in [MAS, MAS[::-1]]) and \
                        ([grid[row + 1][col - 1], grid[row][col], grid[row - 1][col + 1]] in [MAS, MAS[::-1]]):
                    count += 1
    return count


if __name__ == '__main__':
    print(part1(read_file()))
    print(part2(read_file()))
