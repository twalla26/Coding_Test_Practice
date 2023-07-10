T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))

    idx = 0
    res = 0

    for i in range(N):
        while idx < M:
            if A[i] > B[idx]:
                idx += 1
            else:
                break
            
        res += idx
    print(res)