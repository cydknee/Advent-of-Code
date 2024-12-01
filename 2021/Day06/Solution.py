with open('Input/Day6.txt') as file:
    input = file.readline().split(',')
    input = [ int(x) for x in input ]

#input = [ int(x) for x in open('Input/Day6Test.txt').readline().split(',') ]

def calcFish(days):
    fish = [ input.count(f) for f in range(9) ]

    for d in range(days):
        toSpawn = fish.pop(0)
        fish[6] += toSpawn
        fish.append(toSpawn)
    
    return sum(fish)

print('part 1: ', calcFish(80)) # 391671 
print('part 2: ', calcFish(256)) # 1754000560399 
