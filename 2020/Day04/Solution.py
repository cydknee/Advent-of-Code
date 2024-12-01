""" Day 4: Passport Processing """

import re

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        return [[[z for z in y.split(":")] for y in x.split()] for x in file.read().split("\n\n")]


def check_passport(passports):
    valid_passports = []
    for passport in passports:
        prefixes = [item[0] for item in passport]
        if all(item in prefixes for item in ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']):
            valid_passports.append(passport)
    return valid_passports


def check_data(passport):
    for prefix, data in passport:
        match prefix:
            case 'byr':
                if not data.isnumeric() or (int(data) < 1920 or int(data) > 2002):
                    return 0
            case 'iyr':
                if not data.isnumeric() or (int(data) < 2010 or int(data) > 2020):
                    return 0
            case 'eyr':
                if not data.isnumeric() or (int(data) < 2020 or int(data) > 2030):
                    return 0
            case 'ecl':
                if data not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    return 0
            case 'pid':
                if not re.search('^[0-9]{9}$', data):
                    return 0
            case 'hcl':
                if not re.search('^#[0-9a-f]{6}$', data):
                    return 0
            case 'hgt':
                if not re.search('(^[0-9]{3}cm)$|(^[0-9]{2}in)$', data):
                    return 0
                if data[-2::] == "cm" and (int(data[:3:]) < 150 or int(data[:3:]) > 193):
                    return 0
                if data[-2::] == "in" and (int(data[:2:]) < 59 or int(data[:2:]) > 76):
                    return 0
    return 1


def part1():
    return len(check_passport(read_file()))


def part2():
    valid = 0
    for passport in check_passport(read_file()):
        valid += check_data(passport)
    return valid


if __name__ == '__main__':
    print(part1())  # 206
    print(part2())  # 123
