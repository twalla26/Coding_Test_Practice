numOfGoals = int(input())

scoreList = [0, 0]
record = {"00:00": "0:0"} # 시각 00:00에 점수는 0:0

result1 = "00:00"
result2 = "00:00"

for i in range(numOfGoals):
    team, time = input().split()
    if team == '1':
        scoreList[0] += 1
    else:
        scoreList[1] += 1

    score = str(scoreList[0]) + ':' + str(scoreList[1])
    record[time] = score

record["48:00"] = "?:?"

timeRecord = list(record.keys())
scoreRecord = list(record.values())


def subTime(time1, time2):
    min1, sec1 = time1.split(':')
    min2, sec2 = time2.split(':')

    min1 = int(min1)
    sec1 = int(sec1)
    min2 = int(min2)
    sec2 = int(sec2)

    time1 = min1 * 60 + sec1
    time2 = min2 * 60 + sec2

    result = time1 - time2
    min = result // 60
    sec = result % 60

    if min < 10:
        min = '0' + str(min)
    else:
        min = str(min)

    if sec < 10:
        sec = '0' + str(sec)
    else:
        sec = str(sec)

    return min + ':' + sec

def addTime(time1, time2):
    min1, sec1 = time1.split(':')
    min2, sec2 = time2.split(':')

    min1 = int(min1)
    sec1 = int(sec1)
    min2 = int(min2)
    sec2 = int(sec2)

    time1 = min1 * 60 + sec1
    time2 = min2 * 60 + sec2

    result = time1 + time2
    min = result // 60
    sec = result % 60

    if min < 10:
        min = '0' + str(min)
    else:
        min = str(min)

    if sec < 10:
        sec = '0' + str(sec)
    else:
        sec = str(sec)

    return min + ':' + sec


for i in range(numOfGoals+1):
    targetScore = scoreRecord[i]
    if targetScore == "?:?":
        break
    score1, score2 = targetScore.split(':')
    
    if int(score1) > int(score2):
        difference = subTime(timeRecord[i + 1], timeRecord[i])
        result1 = addTime(result1, difference)
    elif int(score1) < int(score2):
        difference = subTime(timeRecord[i + 1], timeRecord[i])
        result2 = addTime(result2, difference)
    else:
        continue

print(result1)
print(result2)
