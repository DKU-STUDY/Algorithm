from itertools import combinations

N, M = map(int, input().split())
satifies = [list(map(int, input().split())) for _ in  range(N)]
res = 0
for chickens in combinations(range(M), 3):
    total = 0
    for satify in satifies:
        unit = max(satify[chickens[0]], satify[chickens[1]], satify[chickens[2]])
        total += unit
    res = max(res, total)

print(res)