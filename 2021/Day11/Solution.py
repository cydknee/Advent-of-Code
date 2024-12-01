with open('Input/Day11Test.txt') as file:
    input = [[ int(x) for x in i ] for i in file.read().splitlines() ] # 10 x 10 martix

totalFlashes, flashes, steps = 0,0,0
adjacent = [(0, -1), (-1, 0), (0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

while flashes != 100:
    flashes = 0
    somethingChanged = True
    
    input = [[ i + 1 for i in line ] for line in input ] #increase energy by 1

    while somethingChanged:
        somethingChanged = False
        for x in range(len(input)):
            for y in range(len(input[x])):
                if input[x][y] > 9:
                    somethingChanged = True
                    input[x][y] = 0
                    flashes += 1
                    
                    for adj_x, adj_y in adjacent:
                        adj_x += x
                        adj_y += y
                        if adj_x >=0 and adj_x < len(input) and adj_y >= 0 and adj_y < len(input[x]) and input[adj_x][adj_y] != 0:
                            input[adj_x][adj_y] += 1
            
    totalFlashes += flashes

    steps += 1
    if steps == 100:
        partOne = totalFlashes

print('part 1: ', partOne) # 1615   Test: 1656
print('part 2: ', steps) # 249  Test: 195