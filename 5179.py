def participantInfo(submitList, id):
    mySubmitList = []
    myScore = 0
    numOfHits = 0
    for i in submitList:
        if (i[0] == id):
            mySubmitList.append(i)
    for i in mySubmitList:
        wrongCnt = 0 # 문제당 틀린 횟수
        if i[3] == 0: # 오답일 경우
            pass
        else: # 정답일 경우
            firstAnswer = True
            for j in range(mySubmitList.index(i)): # 이전 제출목록들 중에서
                if mySubmitList[j][1] == i[1]: # 같은 문제들 중에서
                    if mySubmitList[j][3] == 1: # 정답이 있다면 (풀었던 문제를 또 맞춤)
                        firstAnswer = False
                        break
                    else: # 오답이있다면
                        wrongCnt += 1 # 오답 개수 + 1
            if firstAnswer:
                numOfHits += 1
                myScore += i[2] + 20 * wrongCnt
    return [numOfHits, myScore]

numOfDataSet = int(input())
outputList = [] # 최종적으로 출력할 리스트

for i in range(numOfDataSet):
    numOfQuestion, numOfSubmit, numOfParticipant = map(int, input().split())

    submitList = [] # 모든 제출기록 리스트, [[0, 0, 0, 0], [0, 0, 0, 0], ... ]
    scoreList = [] # [[_, _, _], [_, _, _], ... ] 식으로 각각의 데이터셋에 대한 점수 리스트

    for i in range(numOfSubmit):
        participant, question_number, submit_time, isCorrect = input().split()
        submitList.append([int(participant), question_number, int(submit_time), int(isCorrect)])

    for i in range(numOfParticipant):
        scoreList.append([i+1])
        scoreList[i].extend(participantInfo(submitList, i+1))  

    scoreList.sort(key=lambda x : (-x[1], x[2]))
    outputList.append(scoreList)

for i in range(numOfDataSet):
    print("Data Set %d:"%(i+1))

    for j in outputList[i]:
        print(j[0], j[1], j[2]) 
    print()