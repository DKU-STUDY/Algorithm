N, M = map(int, input().split())

N_set = set()
for _ in range(N):
    N_set.add(input())
res = 0
for _ in range(M):
    if input() in N_set:
        res += 1
print(res)