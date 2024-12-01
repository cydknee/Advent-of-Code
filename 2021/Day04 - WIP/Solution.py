""" Day 4: Giant Squid """

FILE_NAME = "Input.txt"


def read_file():
    with open(FILE_NAME, "r") as file:
        called_numbers = [int(x) for x in file.readline().split(",")]
        bingo_cards = [[[int(z) for z in y.split()] for y in x.splitlines()] for x in file.read()[1::].split("\n\n")]
        return called_numbers, bingo_cards


def play_bingo(called_numbers, bingo_cards, part_one):
    for called_number in called_numbers:
        print(len(bingo_cards))
        mark_card(called_number, bingo_cards)
        winning_card = check_cards(bingo_cards)  # could be more than one winning card in a round
        if winning_card:
            if part_one:
                return count_unmarked(winning_card) * called_number
            else:
                if len(bingo_cards) == 1:
                    return count_unmarked(bingo_cards[0]) * called_number
                else:
                    bingo_cards.remove(winning_card)


def mark_card(called_number, bingo_cards):
    for card in bingo_cards:
        for line in card:
            for number in line:
                if number == called_number:
                    index = line.index(number)
                    line[index] = -1


def check_cards(bingo_cards):
    for card in bingo_cards:
        for line in card:
            if sum(line) == -5:
                return card

        for i in range(len(card[0])):
            if sum([col[i] for col in card]) == -5:
                return card


def count_unmarked(card):
    total = 0
    for line in card:
        for number in line:
            if number > -1:
                total += number
    return total


def part1():
    called_numbers, bingo_cards = read_file()
    return play_bingo(called_numbers, bingo_cards, True)


def part2():
    called_numbers, bingo_cards = read_file()
    return play_bingo(called_numbers, bingo_cards, False)


if __name__ == '__main__':
    # print(part1())  # 5685
    print(part2())  #
