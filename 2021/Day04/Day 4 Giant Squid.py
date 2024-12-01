import numpy as np

with open('e:/projects/Python/Advent/Input/Day4.txt') as file:
    bingoCaller = file.readline().split(',')
    bingoCards = file.read().splitlines()
    bingoCards = list(filter(lambda x: x != '', bingoCards))  

bingo = []

def createCards():
    singleCard = []
    for x in range(len(bingoCards)):
        singleCard.append(bingoCards[x].split())
        
        if (x+1) % 5 == 0:
            bingo.append(singleCard)
            singleCard = []        
    
def markCard():
    for card in bingo:
        for line in card:
            for number in line:
                if str(ball) == number:
                    index = line.index(number)
                    line[index] = 'X'
            
def checkWinningCard(ball):
    for card in bingo:
        c = np.array(card)

        for line in card:
            if line == ['X', 'X', 'X', 'X', 'X']:
                total = countUnmarkedNumbers(card)
                return total*int(ball)

        for x in range(len(c)):
            if ((c[:, x]) == ['X', 'X', 'X', 'X', 'X']).all():
                total = countUnmarkedNumbers(card)
                return total*int(ball)

def checkLoosingCard(ball, bingo):
    for card in bingo:
        c = np.array(card)

        for line in card:
            if line == ['X', 'X', 'X', 'X', 'X']:
                bingo = list(filter(lambda x: x != card, bingo)) 

        for x in range(len(c)):
            if ((c[:, x]) == ['X', 'X', 'X', 'X', 'X']).all():
                bingo = list(filter(lambda x: x != card, bingo)) 
                 
    return bingo

def completeLastCard(ball, bingo):
    total = countUnmarkedNumbers(bingo)
    return total * int(ball)
                    
def countUnmarkedNumbers(card):
    total = 0
    for line in card:
        for number in line:
            if number != 'X':
                total += int(number)
    return total



winnningTotal= None
createCards()
loosingTotal = []

for ball in bingoCaller:
    markCard()
    if not winnningTotal:
        winnningTotal = checkWinningCard(ball)
    if not len(loosingTotal) == 1:    
        loosingTotal = checkLoosingCard(ball, bingo)
    else:
        part2Total = completeLastCard(ball, loosingTotal[0])
        break

print('part 1: ',winnningTotal) # 5685
print('part 2: ',part2Total)  # 21070
