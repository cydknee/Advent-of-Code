""" AoC 2024 Day 2: Red-Nosed Reports """

FILE_NAME = "../../testInput.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        puzzle_input = [x.splitlines() for x in file.read().split("\n\n")]
        input_1 = [[y, z] for y, z in [map(int, x.split("|")) for x in puzzle_input[0]]]
        input_2 = [list(y) for y in [map(int, x.split(",")) for x in puzzle_input[1]]]
        return input_1, input_2


def solution(ordering_rules, updates):
    total = 0
    broken_updates = []
    for update in updates:
        safe_count, checks_after, checks_before = 0, 0, 0
        for index in range(len(update)):
            pages_after = update[index+1:]
            checks_after += len(pages_after)
            rules = [x for x in ordering_rules if x[0] == update[index]]
            safe_count += len([x for x in pages_after if [update[index], x] in rules])

            pages_before = update[:index]
            checks_before += len(pages_before)
            rules = [x for x in ordering_rules if x[1] == update[index]]
            safe_count += len([x for x in pages_before if [x, update[index]] in rules])

        if safe_count == checks_after + checks_before:
            total += update[len(update)//2]
        else:
            broken_updates.append(update)
    return total, broken_updates


def part1(ordering_rules, updates):
    return solution(ordering_rules, updates)[0]


def part2(ordering_rules, updates):
    updates = solution(ordering_rules, updates)[1]
    return len(updates)


if __name__ == '__main__':
    part_1, part_2 = read_file()
    print(part1(part_1, part_2))  # 
    print(part2(part_1, part_2))  #