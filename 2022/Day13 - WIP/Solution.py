""" AoC 2022 Day 13: Distress Signal """

FILE_NAME = "testInput.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [[y for y in x.split()] for x in file.read().split("\n\n")]


def parse_signal_pair(signal):
    return eval(signal[0]), eval(signal[1])


def compare_packets(left, right):
    if type(left) == int and type(right) == int:
        return left - right
    elif type(left) == list and type(right) == int:
        return compare_packets(left, [right])
    elif type(left) == int and type(right) == list:
        return compare_packets([left], right)

    for left_item, right_item in zip(left, right):
        difference = compare_packets(left_item, right_item)
        if difference:
            return difference

    return len(left) - len(right)


def part1():
    correct_order = 0
    signals = read_file()
    for i, signal in enumerate(signals):
        left, right = parse_signal_pair(signal)
        if compare_packets(left, right) < 0:
            correct_order += i + 1
    return correct_order


def part2():
    return None


if __name__ == '__main__':
    print(part1())  #
    print(part2())  #
