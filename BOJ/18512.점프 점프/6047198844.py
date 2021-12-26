X, Y, P1, P2 = map(int, input().split())
if X == Y and P1 != P2:
    print(-1)
else:
    cnt = 0
    S1, S2 = P1, P2
    visited = set()
    while True:
        S1 += X
        S2 += Y
        if S1 in visited:
            print(S1)
            exit()
        if S2 in visited:
            print(S2)
            exit()
        visited.add(S1)
        visited.add(S2)