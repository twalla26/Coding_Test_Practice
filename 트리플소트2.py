N = int(input())
array = input().split()

array = list(map(int, array))

for i in range(N):
    if i % 2: # 홀수 인덱스
        if array[i] % 2 == 0:
            pass
        else:
            print('NO')
            break
    else:
        if array[i] % 2 == 1:
            pass
        else:
            print('NO')
            break
    if i == N - 1:
        print('YES')
        break
        