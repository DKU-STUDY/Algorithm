X, Y, P1, P2 = map(int, input().split())
S1, S2 = P1, P2
visited = set()
visited.add(S1)
visited.add(S2)
for _ in range(100001):
    S1 += X
    S2 += Y
    if S1 in visited:
        print(S1)
        break
    if S2 in visited:
        print(S2)
        break
    visited.add(S1)
    visited.add(S2)
else:
    print(-1)