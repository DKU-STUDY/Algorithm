import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


def func(root, early):
    if memo[root][int(early)] != -1:
        return memo[root][int(early)]

    if early:
        ans = 1
        for child in children[root]:
            ans += min(func(child, True), func(child, False))
    else:
        ans = 0
        for child in children[root]:
            ans += func(child, True)
    memo[root][int(early)] = ans
    return memo[root][int(early)]


N = int(sys.stdin.readline())
edge = [[] for _ in range(N + 1)]
memo = [[-1, -1] for _ in range(N + 1)]

for _ in range(N - 1):
    V, W = map(int, sys.stdin.readline().split())
    edge[V].append(W)

children = [[] for _ in range(N + 1)]

# 트리 생성
# 1번을 루트로한다.
Q = deque([1])
visited = set()
visited.add(1)
while Q:
    root = Q.popleft()

    for child in edge[root]:
        if child not in visited:
            children[root].append(child)
            Q.append(child)
            visited.add(child)

print(min(func(1, True), func(1, False)))
