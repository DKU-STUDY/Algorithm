page = int(input())
res = [0 for i in range(10)]
point = 1
while page != 0:
    while page % 10 != 9:
        for i in str(page):
            res[int(i)] += point
        page -= 1
    if page < 10:
        for i in range(page + 1):
            res[i] += point
        res[0] -= point
        break
    else:
        for i in range(10):
            res[i] += (page // 10 + 1) * point
    res[0] -= point
    point *= 10
    page //= 10
for i in res:
    print(i, end=' ')