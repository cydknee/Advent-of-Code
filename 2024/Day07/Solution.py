""" AoC 2024 Day 7: Bridge Repair """

FILE_NAME = "testInput.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [[int(y.replace(":", "")) for y in x.split(" ")] for x in file.read().split("\n")]


def produce_tree(values, limit):
    queue = [values[0]]

    for v in values[1:]:
        new_queue = []

        for q in queue:
            summation = v + q
            product = v * q
            print(f"v = {v}, q = {q}, summation = {summation}, product = {product} ")

            if summation <= limit:
                new_queue.append(summation)

            if product <= limit:
                new_queue.append(product)
            print(f"{new_queue}")
        queue = new_queue

    output = []

    for q in queue:
        if q == limit:
            output.append(q)

    return output


def part1(reports):
    total = 0

    for line in reports:
        limit = line.pop(0)
        values = line

        tree = produce_tree(values, limit)

        if len(tree) == 0:
            continue

        total += limit

    return total


def part2(reports):
    return None


if __name__ == '__main__':
    print(part1(read_file()))  #
    print(part2(read_file()))  #