from itertools import product

N, M = map(int, input().split())

table = [list(input()) for _ in range(N)]

square = set(root ** 2 for root in range(0, 31622 + 1))
ans = -1
for y in range(N):
    for x in range(M):
        for dy, dx in product(range(-8, 8 + 1), repeat=2):
            num = ''
            ny, nx = y, x
            if dy == 0 and dx == 0:
                continue

            while 0 <= ny < N and 0 <= nx < M:
                num += table[ny][nx]
                ny += dy
                nx += dx
                if int(num) in square:
                    ans = max(ans, int(num))
print(ans)
