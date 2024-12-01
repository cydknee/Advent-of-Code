with open('Input/Day10.txt') as file:
    input = file.read().splitlines()

partOne, partTwo = 0,0
scores = []
points = { ')':3, ']':57, '}':1197, '>':25137 }

for line in input:
    removedPair = True
    while removedPair:
        startlen = len(line)
        line = line.replace('()', '').replace('[]', '').replace('{}', '').replace('<>', '')
        removedPair = startlen != len(line)

    bracket = next((bracket for bracket in line if bracket in points), None) 
    if bracket is not None:
        partOne += points[bracket]
    else:
        score = 0
        for bracket in reversed(line):
            score = score * 5 + '([{<'.index(bracket) + 1
        scores.append(score)

partTwo = sorted(scores)[len(scores) // 2]

print('part 1: ', partOne) # 321237      Test: 26397
print('part 2: ', partTwo) # 2360030859  Test: 288957