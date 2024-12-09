""" AoC 2024 Day 5: Print Queue """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        puzzle_input = [x.splitlines() for x in file.read().split("\n\n")]
        rules = [[y, z] for y, z in [map(int, x.split("|")) for x in puzzle_input[0]]]
        updates = [list(y) for y in [map(int, x.split(",")) for x in puzzle_input[1]]]
        return rules, updates


def bubble_sort(updates, rules):
    changed = False
    for i in range(len(updates)):
        for j in range(i+1, len(updates)):
            if [updates[j], updates[i]] in rules:
                updates[j], updates[i] = updates[i], updates[j]
                changed = True
    return changed


def part_1_and_2():
    sorted_total, unsorted_total = 0, 0
    rules, updates = read_file()
    for instructions in updates:
        if bubble_sort(instructions, rules):
            unsorted_total += instructions[len(instructions) // 2]
        else:
            sorted_total += instructions[len(instructions) // 2]
    return sorted_total, unsorted_total


if __name__ == '__main__':
    part_1, part_2 = part_1_and_2()
    print(part_1)  # 5762
    print(part_2)  # 4130
