def swap(sy, sx, ey, ex):
    for y in range(sy, ey + 1):
        for x in range(sx, ex + 1):
            if A[y][x] == '0':
                A[y][x] = '1'
            else:
                A[y][x] = '0'


N, M = map(int, input().split())

A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(N)]

# N, M 이 3보다 작은 경우.
if N < 3 or M < 3:
    if A == B:
        print(0)
    else:
        print(-1)
    exit()

res = 0
for y in range(N-2):
    for x in range(M-2):
        if A[y][x] != B[y][x]:
            swap(y, x, y + 2, x + 2)
            res += 1

if A == B:
    print(res)
else:
    print(-1)

