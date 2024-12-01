from collections import Counter

with open('Input/Day5.txt') as file:
    input = file.read().splitlines()
    input = [ x.replace(' ->', '').split() for x in input ]
    input = [[[ int(i) for i in input[c][0].split(',') ] , [ int(i) for i in input[c][1].split(',') ]] for c in range(len(input))]

oceanFloor = []

def horizontal(coord1, coord2):
    if coord1[1] > coord2[1]:
        temp = coord1
        coord1 = coord2
        coord2 = temp

    while coord1 != coord2:
        oceanFloor.append(str(coord1))
        coord1 = [coord1[0], coord1[1] + 1]

    oceanFloor.append(str(coord1))

def vertical(coord1, coord2):
    if coord1[0] > coord2[0]:
        temp = coord1
        coord1 = coord2
        coord2 = temp

    while coord1 != coord2:
        oceanFloor.append(str(coord1))
        coord1 = [coord1[0] + 1, coord1[1]]

    oceanFloor.append(str(coord1))

def diagonal(coord1, coord2):
    if coord1[0] > coord2[0]:
        temp = coord1
        coord1 = coord2
        coord2 = temp

    if coord1[1] > coord2[1]: # moving down
        while coord1 != coord2:
            oceanFloor.append(str(coord1))
            coord1 = [coord1[0] + 1, coord1[1] - 1]
    elif coord1[1] < coord2[1]: # moving up
        while coord1 != coord2:
            oceanFloor.append(str(coord1))
            coord1 = [coord1[0] + 1, coord1[1] + 1]

    oceanFloor.append(str(coord1))


for coord in input:
    c1 = coord[0]
    c2 = coord[1]

    if c1[0] == c2[0]:
        horizontal(c1, c2)
    elif c1[1] == c2[1]:
        vertical(c1, c2)
    else:
        diagonal(c1, c2)

listOfKeys = [key  for (key, value) in Counter(oceanFloor).items() if value > 1]

print('part 1: ', len(listOfKeys)) # 6189 & 19164