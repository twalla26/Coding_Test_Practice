
size, amount = input().split()
numIndex = []
numIndex = map(int, input().split())

size = int(size)

queue = []
for i in range(size):
    queue.append(i + 1)

cnt = 0
for i in numIndex:
    if (queue[0] == i):
        firstNum = queue.pop(0)
        size -= 1
    else:
        if (queue.index(i) <= (size / 2)):
            cnt += queue.index(i)
            enque = queue.index(i)
            for i in range(enque):
                firstNum = queue.pop(0)
                queue.append(firstNum)
            queue.pop(0)
            size -= 1
        else:
            cnt += size - queue.index(i)
            deque = size - queue.index(i)
            for i in range(deque):
                lastNum = queue.pop()
                queue.insert(0, lastNum)
            queue.pop(0)
            size -= 1

print(cnt)
    