numOfCase = int(input())
result = []

for i in range(numOfCase):
    numOfA, numOfB = map(int, input().split())
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))

    cnt = 0
    for j in range(numOfA):
        for k in range(numOfB):
            if A[j] > B[k]:
                cnt += 1
            else:
                break
            
print(*result)
