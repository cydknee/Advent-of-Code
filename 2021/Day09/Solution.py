with open('Input/Day9Test.txt') as file:
    input = file.read().splitlines()

riskLevel, basin, numberOfBasins = 0, 0, 0
basinCoordinates = []

def compare(coordOne, coordTwo):
    if (coordOne[0] == coordTwo[0] and coordOne[1]+1 == coordTwo[1]) \
        or (coordOne[0]+1 == coordTwo[0] and coordOne[1] == coordTwo[1]) \
        or (coordOne[0] == coordTwo[0] and coordOne[1]-1 == coordTwo[1]) \
        or (coordOne[0]-1 == coordTwo[0] and coordOne[1] == coordTwo[1]):
            return True
    else:
        return False

for previousLine,currentLine,nextLine in zip([None]+input[:-1], input, input[1:]+[None]):
    currentLine = [ int(num) for num in currentLine ]
    index = 0
    for previousNum,currentNum,nextNum in zip([None]+currentLine[:-1], currentLine, currentLine[1:]+[None]):
        if (previousNum == None or previousNum > currentNum) \
            and (nextNum == None or currentNum < nextNum) \
            and (previousLine == None or int(previousLine[index]) > currentNum) \
            and (nextLine == None or int(nextLine[index]) > currentNum):
                riskLevel += (1 + currentNum)
                numberOfBasins += 1

        index += 1

print('part 1: ', riskLevel)  # 532

basins = []

for row in range(len(input)):
    input[row] = [ int(num) for num in input[row] ]
    for column in range(len(input[row])):
        if input[row][column] != 9:
            basinCoordinates.append([row, column])

currentBasin = []

print('basinCoordinates', basinCoordinates)
print('currentBasin', currentBasin)

while len(basinCoordinates) > 0:
    currentBasin = []
    currentBasin.append(basinCoordinates.pop(0))
    addedCoord = True
    #print('------------------')
    while addedCoord:
        addedCoord = False
        for coord in currentBasin:
            #print(basinCoordinates)
            for coordinate in basinCoordinates:
                #print(coord, coordinate)
                if compare(coord, coordinate):
                    currentBasin.append(coordinate)
                    basinCoordinates.remove(coordinate)
                    addedCoord = True
    basins.append(currentBasin)

    print(len(basinCoordinates), basinCoordinates)

print('basinCoordinates', basinCoordinates)
print('currentBasin', currentBasin)
print('Basins', basins)


totals = []
for basin in basins:
    totals.append(len(basin))
totals.sort(reverse=True)

print('part 2: ', totals[0]*totals[1]*totals[2]) # 1110780