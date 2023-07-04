n = int(input())
inputNum = list(str(n))
print(inputNum)
isChanged = False
for i in range(len(inputNum) - 1):
    backIdx = - (i + 1)
    if inputNum[backIdx - 1] < inputNum[backIdx]:
        swapNum1 = inputNum[backIdx - 1]

        min = inputNum[backIdx]
        minIdx = 0
        for j in range(-backIdx):
            tempIdx = j + backIdx
            print('tempIdx:', tempIdx)
            if inputNum[tempIdx] > swapNum1 and inputNum[tempIdx] <= min:
                min = inputNum[tempIdx]
                minIdx = tempIdx
                print(tempIdx)

        print('min:', min)
        print('swapNum1:', inputNum[backIdx - 1], 'swapNum2:', inputNum[minIdx])
        print('backIdx - 1:', backIdx - 1, 'minIdx:', minIdx)
        inputNum[backIdx - 1], inputNum[minIdx] = inputNum[minIdx], inputNum[backIdx - 1]
        print(inputNum)

        tempList = inputNum[backIdx:]
        tempList.sort()
        inputNum = inputNum[:backIdx]
        inputNum.extend(tempList)

        result = ""
        for i in inputNum:
            result += i
        
        result = int(result)
        isChanged = True
        print(result) # 165
        break
    
if not isChanged:
    print(0)

