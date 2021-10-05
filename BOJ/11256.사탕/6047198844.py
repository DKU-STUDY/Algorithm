#사탕들을 포장할 공간은 충분하다.

T = int(input())
for _ in range(T):
    J, N = map(int, input().split())
    boxs = list()
    for _ in range(N):
        R, C = map(int, input().split())
        boxs.append(R*C)
    boxs.sort(reverse=True)
    cnt = 0
    for box in boxs:
        J -= box
        cnt += 1
        if J <= 0:
            print(cnt)
            break