def alarm(time):
    TIME_SEPARATE = 45
    time += 2400
    minute = int(str(time)[0:2]) * 60 + int(str(time)[2:4]) - TIME_SEPARATE
    hh = (minute // 60) % 24
    mm = minute % 60
    return str(hh) + "시 " + str(mm)+"분"

