""" AoC 2022 Day 6: Tuning Trouble """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return file.read()


def read_communications_system(data_stream, marker_length):
    for marker in range(0, len(data_stream)-(marker_length - 1)):
        read_packets = data_stream[marker:marker + marker_length]
        if len(set(read_packets)) == len(read_packets):
            return marker + marker_length


def part1():
    return read_communications_system(read_file(), 4)


def part2():
    return read_communications_system(read_file(), 14)


if __name__ == '__main__':
    print(part1())
    print(part2())
