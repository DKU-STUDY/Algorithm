import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
# 최대 로그 깊이
LOG = 16

N = int(input())
edge = [[] for _ in range(N + 1)]
# 트리 만들기
for _ in range(N - 1):
    i, j = map(int, input().split())
    edge[i].append(j)
    edge[j].append(i)

# 부모 노드 정보
# P[i][k] = i의 2^k 번째 조상.
# P[i][k] = P[P[i][k-1]][k-1]
P = [[0] * (LOG + 1) for _ in range(N + 1)]

# 노드 방문 정보
visited = set()

# 노드의 깊이 정보
depth = [0] * (N + 1)


# 깊이 탐색하면서 단방향 그래프로 만든다.
def dfs(parent, d):
    visited.add(parent)
    depth[parent] = d

    for child in edge[parent]:
        if child in visited:
            continue
        # 부모 노드 정보 갱신
        P[child][0] = parent
        dfs(child, d + 1)


# 전체 부모 관계를 갱신한다.
def set_parent():
    # 위에서 부터 깊이를 더한다.
    # 0 번째 깊이는 이미 단방향 그래프 제작과정에서 만들어짐
    for i in range(1, LOG + 1):
        for j in range(1, N + 1):
            P[j][i] = P[P[j][i - 1]][i - 1]


# A, B 의 공통조상을 찾는다.
def LCA(A, B):
    # 항상 B가 깊도록 설정한다.
    if depth[A] > depth[B]:
        A, B = B, A

    # 깊이를 조정한다.
    # 이때 P를 사용해서 로그 탐색이 이루어진다.
    # 비트 연산을 이용한다.
    for i in range(LOG, -1, -1):
        # 깊이 차이가 i 보다 같거나 크면 i 만큼 점프 할 수 있다.
        if depth[B] - depth[A] >= (1 << i):
            B = P[B][i]

    # 둘이 같으면 종료한다.
    if A == B:
        return A

    # 조상을 향해 거슬러올라간다. 로그만큼 거슬러 올라간다.
    # 최소 공통 조상의 직전 자식을 찾을것이다.
    for i in range(LOG, -1, -1):
        # 같으면 최소 공통 조상의 직전 자식의 조건이 되지 않는다.
        # 같지않다면 최소 공통 조상의 직전 자식의 조건이 된다.
        if P[A][i] != P[B][i]:
            A = P[A][i]
            B = P[B][i]

    # 최소 공통 조상의 직전 자식의 부모가 정답이다.
    return P[A][0]


# 루트는 1번이다. 부모관계 설정. 간선을 만든다.
dfs(1, 0)
set_parent()

M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    print(LCA(i, j))