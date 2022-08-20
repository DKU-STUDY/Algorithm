import datetime
import sys

N = int(input())
flowers = list()
for _ in range(N):
    start_month, start_day, end_month, end_day = map(int, sys.stdin.readline().split())
    start = datetime.date(2020, start_month, start_day)
    if end_month == 12:
        end = datetime.date(2020, end_month, 1)
    else:
        end = datetime.date(2020, end_month, end_day)
    flowers.append((start, end))
flowers.append((datetime.date(2020, 12, 31), datetime.date(2020, 12, 31)))
flowers.sort()
# 첫꽃은 3월 1일에 피어야한다.
cur_flower = (datetime.date(2020, 1, 1), datetime.date(2020, 3, 1))
last_flower = (datetime.date(2020, 1, 1), datetime.date(2020, 3, 1))
res = 0
for i in range(len(flowers)):
    # 범위 사이에 존재하는 경우.
    if flowers[i][0] <= cur_flower[1] <= flowers[i][1] and flowers[i][1] > last_flower[1]:
        last_flower = flowers[i]
    # 범위안에 존재하는 경우.
    elif cur_flower[0] <= flowers[i][0] and flowers[i][1] <= cur_flower[1]:
        pass
    # 범위 사이에 존재하지 않는 경우.
    else:
        # 갱신이 안된 경우.
        if cur_flower == last_flower:
            print(0)
            exit()

        # 갱신
        cur_flower = last_flower
        res += 1
        # 갱신 된 꽃 사이에 존재하면 갱신.
        if flowers[i][0] <= cur_flower[1] <= flowers[i][1]:
            last_flower = flowers[i]

cur_flower = last_flower
# 마지막꽃은 12월 1일 이후에 져야한다.
if cur_flower[1] <= datetime.date(2020, 11, 30):
    print(0)
    exit()
print(res)