N = int(input())
ropes = list()
for _ in range(N):
    ropes.append(int(input()))
ropes.sort(reverse=True)
print(max([(idx + 1) * rope for idx, rope in enumerate(ropes)]))
