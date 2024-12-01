""" Day 3: Binary Diagnostic """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [list(map(int, x)) for x in file.read().splitlines()]


def get_gamma_or_epsilon(report, is_gamma):
    rate = []
    for i in range(len(report[0])):
        common_bit = sum([col[i] for col in report]) >= len(report) / 2
        rate.append(int(common_bit) if is_gamma else int(not common_bit))
    return rate


def life_support_rating(report, is_gamma):
    for i in range(len(report[0])):
        criteria = get_gamma_or_epsilon(report, is_gamma)
        report = [line for line in report if line[i] == criteria[i]]
        if len(report) == 1:
            break
    return "".join(map(str, report[0]))


def calculate_power_consumption(gamma, epsilon):
    g = "".join(map(str, gamma))
    e = "".join(map(str, epsilon))
    return int(g, 2) * int(e, 2)


def part1():
    report = read_file()
    gamma = get_gamma_or_epsilon(report, True)
    epsilon = get_gamma_or_epsilon(report, False)
    return calculate_power_consumption(gamma, epsilon)


def part2():
    report = read_file()
    oxygen = life_support_rating(report, True)
    carbon = life_support_rating(report, False)
    return int(oxygen, 2) * int(carbon, 2)


if __name__ == '__main__':
    print(part1())  # 841526
    print(part2())  # 4790390
