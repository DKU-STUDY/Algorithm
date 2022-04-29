import sys
from collections import defaultdict, deque

N = int(sys.stdin.readline())
indegrees = [0 for _ in range(N+1)]
edges = defaultdict(list)
times = [0 for _ in range(N+1)]

for V in range(1, N + 1):
    cmd = list(map(int, sys.stdin.readline().split()))
    times[V] = cmd[0]
    for W in cmd[1:-1]:
        edges[W].append(V)
        indegrees[V] += 1

Q = deque()
res = [0 for _ in range(N+1)]
for V in range(1, N+1):
    if indegrees[V] == 0:
        Q.append(V)
        res[V] = times[V]

while Q:
    V = Q.popleft()

    for W in edges[V]:
        indegrees[W] -= 1
        res[W] = max(res[V] + times[W], res[W])
        if indegrees[W] == 0:
            Q.append(W)

for V in range(1, N+1):
    print(res[V])