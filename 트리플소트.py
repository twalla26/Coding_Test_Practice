N = int(input())
array = input().split()

array = list(map(int, array))

isSorted = False
while not isSorted:
    isChanged = False
    for i in range(N - 2):
        # 트리플 정렬
        if array[i] > array[i + 2]:
            array[i], array[i + 2] = array[i + 2], array[i]
            isChanged = True

    # 정렬 여부 확인
    for i in range(N - 1):
        if array[i] > array[i + 1]: # 조건에 걸리면 정렬 안됨.
            if not isChanged:
                print('NO')
                isSorted = True # 부분적으로만 정렬됨.
                break
            else:
                break
        if i == N - 2:
            print('YES')
            isSorted = True
            break