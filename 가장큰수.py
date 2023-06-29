def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers)) # ['6', '10', '2']

    isBiggist = True
    digit = 0 # 자릿수
    while isBiggist:
        for i in range(len(numbers) - 1):
            for j in range(i+1, len(numbers) - 1):
                if (i[digit] == j[digit]):
                    digit += 1
                    

        

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))

