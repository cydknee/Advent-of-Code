with open('Input/Day14.txt') as file:
    input = file.readline().strip('\n')
    rule = filter(None, file.read().splitlines())

rules, polymer, temp, letters = {}, {}, {}, {}

for line in rule: # create all the dictionaries
    key, value = line.strip().split(' -> ')
    rules[key] = value
    polymer[key] = temp[key] = 0
    if value not in letters:
        letters[value] = 0

for (previous, current) in zip(input, input[1:]): # Add first input to dictionary
    polymer.update({str(previous) + str(current): polymer[key] + 1})

for step in range(40):
    for key in polymer:
        if polymer[key] != 0:
            element = rules[key]
            amount = polymer[key]

            temp.update({key[0]+element : temp[key[0]+element] + amount})
            temp.update({element+key[1] : temp[element+key[1]] + amount})

            polymer.update({ key : 0 })

    for key in polymer:
        polymer.update({key: temp[key]})
        temp.update({key: 0})

for item in polymer:
    letters[item[0]] += polymer[item]

letters[input[-1]] += 1

max = max(letters.keys(), key=(lambda k: letters[k]))
min = min(letters.keys(), key=(lambda k: letters[k]))

print('solution:', letters[max] - letters[min]) # part 1 2170    part 2 2422444761283