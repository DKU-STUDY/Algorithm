import sys

N, M = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

prefix_sum = [0]
for y in range(N):
    for x in range(N):
        prefix_sum.append(table[y][x] + prefix_sum[-1])

for i in range(len(prefix_sum)):
    print(i, prefix_sum[i])
print()
for _ in range(M):
    i, j, y, x = map(lambda i: int(i) - 1, sys.stdin.readline().split())
    k = prefix_sum[y * N + x] - prefix_sum[i * N + j] + table[j-1][i-1]
    print(prefix_sum[y * N + x])
    print(prefix_sum[i * N + j])
    print(table[j-1][i-1])
    print(k)
    print()