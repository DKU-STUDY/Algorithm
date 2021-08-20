import datetime
import collections


def convert_to_time(time):
    hour = time // 3600
    time -= hour * 3600
    minute = time // 60
    time -= minute * 60
    sec = time
    return str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(sec).zfill(2)


def convert_to_sec(time):
    hour, minute, sec = map(int, time.split(':'))
    return hour * 3600 + minute * 60 + sec


def solution(play_time, adv_time, logs):
    answer = ''
    logs.sort()
    times = []

    for log in logs:
        start_time, end_time = map(convert_to_sec, log.split('-'))
        times.append((start_time, end_time))

    arr = [0] * 360001

    window = collections.deque()
    longest_time = 0
    cur_time = 0
    adv_time = convert_to_sec(adv_time)
    play_time = convert_to_sec(play_time)

    # 변화량 기록
    for start_time, end_time in times:
        arr[start_time] += 1
        arr[end_time] -= 1

    # 해당 변화량으로 배열을 채운다.
    for idx in range(1, 360001):
        arr[idx] += arr[idx - 1]

    # 윈도우를 이용, 정답을 구한다.
    maxval = sum(arr[:adv_time])
    maxtime = 0
    curval = maxval

    for i in range(0, 360001 - adv_time):
        curval = curval - arr[i] + arr[i + adv_time]
        if curval > maxval:
            maxval = curval
            maxtime = i + 1

    return convert_to_time(maxtime)