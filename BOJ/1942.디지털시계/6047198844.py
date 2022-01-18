# 문제
#
# 디지털시계는 일반적으로 시각을 “hh:mm:ss”의 형태로 표현한다. hh는 00 이상 23 이하의 값을, mm과 ss는 00 이상 59 이하의 값을 가질 수 있다.
# 이러한 형태의 시각에서 콜론(“:”)을 제거하면 “hhmmss”라는 정수를 얻을 수 있는데, 이러한 정수를 시계 정수라고 한다.
# 이 문제에서 시간이란 시각의 구간을 나타낸다. 예를 들어 [00:59:58, 01:01:24]와 같이 시작하는 시각과 끝나는 시각으로 이루어진 구간을 우리는 시간이라고 부른다. (이러한 구간에는 시작하는 시간과 끝나는 시간도 포함된다)
# 시간이 시작하는 시각과 끝나는 시각으로 주어졌을 때, 이 구간에 포함되는 시계 정수들 중, 3의 배수인 것의 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 세 개의 입력이 주어진다. 첫째 줄부터 세 줄에 걸쳐 시작하는 시각과 끝나는 시각이 “hh:mm:ss”의 형태로 주어진다. 시작하는 시각과 끝나는 시각 사이에는 빈 칸이 하나 있어서, 한 줄마다 (빈 칸을 포함하여) 총 17글자가 입력으로 주어진다. 시작하는 시각과 끝나는 시각은 항상 다르다.
#
# 출력
# 첫째 줄부터 세 개의 줄에 걸쳐 입력된 구간에 포함되는 시계 정수들 중, 3의 배수인 것의 개수를 출력한다. 입력된 순서대로 각 줄에 한 개씩 차례로 출력하면 된다.
import datetime

time_range = [input().split() for _ in range(3)]
FMT = '%H:%M:%S'

for start_time, end_time in time_range:
    start_time, end_time = datetime.datetime.strptime(start_time, FMT), datetime.datetime.strptime(end_time, FMT)
    res = int((int(str(start_time.hour).zfill(2) + str(start_time.minute).zfill(2) + str(start_time.second).zfill(2))) % 3 == 0)
    while start_time.hour != end_time.hour or start_time.minute != end_time.minute or start_time.second != end_time.second:
        start_time = start_time + datetime.timedelta(seconds=1)
        if (int(str(start_time.hour).zfill(2) + str(start_time.minute).zfill(2) + str(start_time.second).zfill(2))) % 3 == 0:
            res += 1
    print(res)