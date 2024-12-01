""" Day 2: Password Philosophy """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [[y for y in x.split(": ")] for x in file.read().splitlines()]


def test_password(passwords):
    valid_amount, valid_position = 0, 0
    for rule, password in passwords:
        amount, letter = rule.split()
        start, end = amount.split("-")

        if int(start) <= password.count(letter) <= int(end):
            valid_amount += 1

        if (password[int(start) - 1] == letter and password[int(end) - 1] != letter) \
                or (password[int(start) - 1] != letter and password[int(end) - 1] == letter):
            valid_position += 1
    return valid_amount, valid_position


def part1():
    return test_password(read_file())[0]


def part2():
    return test_password(read_file())[1]


if __name__ == '__main__':
    print(part1())  # 614
    print(part2())  # 354
