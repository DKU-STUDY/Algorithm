from collections import Counter

N, M = map(int, input().split())

table = Counter()
for _ in range(N):
    table.update(list(input()))

#최대 9자리수. -> 123456789
for root in range(11112, 4-1, -1):
    num = str(root ** 2)
    # 등차 수열?
    flag = True
    if len(num) > 1:
        # 공차
        d = int(num[1]) - int(num[0])
        for idx in range(2, len(num)):
            if int(num[idx]) - int(num[idx-1]) != d:
                flag = False
                break
    # 숫자가 표에 있음?
    if flag:
        for i in Counter(num).items():
            print(i)

        break
else:
    print(-1)