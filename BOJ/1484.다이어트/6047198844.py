import sys

G = int(sys.stdin.readline())
arr = list()
# i = x+y
# j = x-y
for i in range(G, 0, -1):
    # 나누어 떨어진다면.
    if G % i == 0:
        j = G // i
        if j > i:
            break
        x = (i + j) // 2
        y = (i - j) // 2
        if y > 0 and (i + j) % 2 == 0:
            arr.append((i + j) // 2)
arr.sort()
if arr:
    for i in arr:
        print(i)
else:
    print(-1)

# 4
