numOfCase = int(input())
result = []

for i in range(numOfCase):
    numOfA, numOfB = input().split()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0

    for a in A:
        for b in B:
            if a > b:
                cnt += 1

    result.append(cnt)

print(*result)