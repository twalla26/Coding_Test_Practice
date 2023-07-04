n = int(input())  # 입력 수 X
inputNum = list(str(n))  # X를 문자열로 변환하여 리스트로 저장

# 뒤에서부터 인접한 숫자를 비교하여 바꿀 위치를 찾음
changeIdx = -1
for i in range(len(inputNum) - 1, 0, -1):
    if inputNum[i - 1] < inputNum[i]:
        changeIdx = i - 1
        break

if changeIdx == -1:
    print(0)  # 바꿀 위치가 없으면 0 출력
else:
    # 바꿀 위치 이후의 숫자들 중 가장 작은 값을 찾아서 교환
    for i in range(len(inputNum) - 1, changeIdx, -1):
        if inputNum[changeIdx] < inputNum[i]:
            inputNum[changeIdx], inputNum[i] = inputNum[i], inputNum[changeIdx]
            break

    # 바꿀 위치 이후의 숫자들을 오름차순으로 정렬
    inputNum[changeIdx + 1:] = sorted(inputNum[changeIdx + 1:])

    result = int(''.join(inputNum))
    print(result)  # 결과 출력