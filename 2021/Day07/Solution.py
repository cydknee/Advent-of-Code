input = [ int(x) for x in open('Input/Day7.txt').readline().split(',') ]
distances = [ int(x + 1) for x in range(max(input)) ]

minp1, minp2 = None, None

for i in range(max(input)):
    p1fuel, p2fuel = 0, 0 
    
    for crab in input:
        move = abs(crab - i)
        p1fuel += move
        p2fuel += sum(distances[:move])
        #p2fuel += sum(count(move))

    if minp1 == None or p1fuel < minp1:
        minp1 = p1fuel

    if minp2 == None or p2fuel < minp2:
        minp2 = p2fuel

print('part 1: ', minp1) # 355150
print('part 2: ', minp2) # 98368490