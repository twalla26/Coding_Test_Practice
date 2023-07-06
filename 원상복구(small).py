numOfCard, numOfMixed = map(int, input().split())
result = list(map(int, input().split()))
D = list(map(int, input().split()))

P = []
origin = []
for i in range(numOfCard):
    P.append(i + 1)
    origin.append(0)

for i in range(numOfMixed):
    S = []
    for i in D:
        S.append(P[i - 1])
    P = S

idx = 0
for i in P:
    origin[i - 1] = result[idx]
    idx += 1

print(*origin)