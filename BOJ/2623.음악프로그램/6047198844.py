import sys
from collections import defaultdict, deque


def union(A, B):
    PA = find(A)
    PB = find(B)

    if PA == PB:
        return False

    P[PB] = PA
    return True


def find(A):
    if P[A] == A:
        return A
    P[A] = find(P[A])
    return P[A]


N, M = map(int, sys.stdin.readline().split())
P = [i for i in range(N + 1)]
lines = [list(map(int, sys.stdin.readline().split()))[1:] for _ in range(M)]
edges = defaultdict(list)
indegrees = [0 for _ in range(N + 1)]

for line in lines:
    for idx in range(len(line) - 1):
        V, W = line[idx], line[idx + 1]
        edges[V].append(W)
        indegrees[W] += 1

# 위상정렬 결과
res = []
# 위상정렬을 위한 큐
Q = deque([])

# indegree 가 0 인 vertex 만 큐에 넣는다.
for i in range(1, N + 1):
    if indegrees[i] == 0:
        Q.append(i)

while Q:
    V = Q.popleft()
    res.append(V)

    for W in edges[V]:
        indegrees[W] -= 1
        if indegrees[W] == 0:
            if not union(V, W):
                print(0)
                exit()
            Q.append(W)


if len(res) != N:
    print(0)
else:
    for r in res:
        print(r)
