rounds = int(input())
myShape = input()
friends = int(input())
friendsShape = []

for i in range(friends):
    friendShape = input()
    friendsShape.append(friendShape)

def RSP(myShape, friendShape):
    score = 0
    if myShape == friendShape:
        score = 1
    else:
        if myShape == 'R' and friendShape == 'S':
            score = 2
        elif myShape == 'S' and friendShape == 'P':
            score = 2
        elif myShape == 'P' and friendShape == 'R':
            score = 2
    return score

def myScore(myShape, friendsShape):
    score = 0
    for i in friendsShape:
        for j in range(len(i)):
            score += RSP(myShape[j], i[j])
    return score

def bestScore(friendsShape): # friendsShape = ['RSPR', 'RPPS', ...]
    score = 0
    shapes = ['R', 'S', 'P']
    for i in range(len(friendsShape[0])):
        friendsShapeDict = {'R': 0, 'S': 0, 'P': 0}
        for j in range(len(friendsShape)):
            friendShape = friendsShape[j][i]
            if friendShape == 'R':
                friendsShapeDict['R'] += 1
            elif friendShape == 'S':
                friendsShapeDict['S'] += 1
            else:
                friendsShapeDict['P'] += 1

        #print(friendsShapeDict) # {'R': 2, 'S': 1, 'P': 1}
    
        valueList = list(friendsShapeDict.values()) # [2, 0, 1]

        scoreList = []
        for i in range(3):
            winningShape = shapes[i]
            tempScore = RSP(winningShape, 'R') * valueList[0] + RSP(winningShape, 'S') * valueList[1] + RSP(winningShape, 'P') * valueList[2]
            scoreList.append(tempScore)
        score += max(scoreList)
    return score
            

print(myScore(myShape, friendsShape))
print(bestScore(friendsShape))
