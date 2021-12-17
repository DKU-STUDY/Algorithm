N, M = map(int, input().split())
bulbs = list(map(int, input().split()))
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        bulbs[b-1] = c
    elif a == 2:
        for idx in range(b-1, c):
            bulbs[idx] += 1
            bulbs[idx] %= 2
    else:
        for idx in range(b-1, c):
            bulbs[idx] = int(a == 4)
for bulb in bulbs:
    print(bulb, end=' ')
