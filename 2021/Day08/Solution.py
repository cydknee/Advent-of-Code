with open('Input/Day8.txt') as file:
    input = file.read().splitlines()
    signal = [ x.split(' | ')[0] for x in input ]
    output = [ x.split(' | ')[1] for x in input ]

count = 0
for line in output:
    for word in line.split():
        if len(word) in [2, 3, 4, 7] :
            count += 1

#print('part 1:', count) # 392

numbers = [0]*10
fourDigitOutput = []
zeroSixNine, twoThreeFive = [], []
grandTotal = 0
total = ''

for line in range(len(signal)):
    for word in signal[line].split():
        word = ''.join(sorted(word))
        match len(word):
            case 2:
                one = [word[i] for i in range(len(word))]
            case 3:
                seven = [word[i] for i in range(len(word))]
            case 4:
                four = [word[i] for i in range(len(word))]
            case 7:
                eight = [word[i] for i in range(len(word))]
            case 6:
                zeroSixNine.append([word[i] for i in range(len(word))])
            case 5:
                twoThreeFive.append([word[i] for i in range(len(word))])

    #print(zeroSixNine)
    #print(twoThreeFive)

    for num in zeroSixNine:
        if len(list(set(num).difference(four))) == 2 :
            nine = num
            zeroSixNine.remove(num)

    for num in zeroSixNine:
        if len(list(set(num).difference(one))) == 4 :
            zero = num
        else :
            six = num

    for num in twoThreeFive:
        #print(len(list(set(num).difference(one))))
        if len(list(set(num).difference(one))) == 3 :
            three = num
            twoThreeFive.remove(num)

    for num in twoThreeFive:
        print(len(list(set(num).difference(nine))))
        if len(list(set(num).difference(nine))) == 0:
            five = num
        else :
            two = num

    
    numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
    print (numbers)
    
    splitOutput = output[line].split()
    print(splitOutput)

    for digit in splitOutput:
        digit = ''.join(sorted(digit))
        print(digit)
        fourDigitOutput.append([digit[i] for i in range(len(digit))])

    for digit in fourDigitOutput :
        for x in range(len(numbers)) :
            if digit == numbers[x]:
                total = total + str(x)
                print(x)
    print(total)

    grandTotal += int(total)
    total = ''
    fourDigitOutput, zeroSixNine, twoThreeFive = [], [], []

    print('part 2: ', grandTotal) # 1004688