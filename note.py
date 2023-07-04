def subTime(time1, time2):
    min1, sec1 = time1.split(':')
    min2, sec2 = time2.split(':')

    min1 = int(min1)
    sec1 = int(sec1)
    min2 = int(min2)
    sec2 = int(sec2)

    time1 = min1 * 60 + sec1
    time2 = min2 * 60 + sec2

    result = time1 - time2
    min = result // 60
    sec = result % 60

    if min < 10:
        min = '0' + str(min)

    if sec < 10:
        sec = '0' + str(sec)

    return str(min) + ':' + str(sec)

def addTime(time1, time2):
    min1, sec1 = time1.split(':')
    min2, sec2 = time2.split(':')

    min1 = int(min1)
    sec1 = int(sec1)
    min2 = int(min2)
    sec2 = int(sec2)

    time1 = min1 * 60 + sec1
    time2 = min2 * 60 + sec2

    result = time1 + time2
    min = result // 60
    sec = result % 60

    if min < 10:
        min = '0' + str(min)

    if sec < 10:
        sec = '0' + str(sec)

    return str(min) + ':' + str(sec)

print(subTime('03:58', '01:59'))

print(int('0'))
print(int('03'))
print('0' + str(9))
print(str('0'))