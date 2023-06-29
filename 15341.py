cardNumber = "" # 입력 받을 카드 번호
cardNumberList = []
resultList = [] # 마지막에 출력할 결과 리스트
isValid = True

while (isValid):
    cardNumber = input()
    if cardNumber == "0000 0000 0000 0000":
        isValid = False
    else:
        cardNumberList.append(cardNumber.replace(" ", ""))

for i in cardNumberList:
    sumOfNum = 0 # 전체 합
    sumOfOdd = 0 # 홀수 합
    sumOfEven = 0 # 짝수 합
    index = 0
    for j in i:
        if (index % 2 == 0): # odd-labeled digit
            tempSum = int(j) * 2
            if (tempSum >= 9):
                tempSum -= 9
            sumOfOdd += tempSum
        else: # even-labeled digit
            sumOfEven += int(j)
        index += 1
    sumOfNum = sumOfOdd + sumOfEven
    if sumOfNum % 10 == 0:
        resultList.append("Yes")
    else:
        resultList.append('No')

for i in resultList:
    print(i)