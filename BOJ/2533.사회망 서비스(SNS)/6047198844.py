import sys

sys.setrecursionlimit(10 ** 9)


# 소셜인 경우와 소셜이 아닌 경우를 계산한다.
def func(root):
    # 방문 처리
    visited[root] = 1
    # 방문한 경우
    memo[root][True] = 1
    for child in edge[root]:
        # 자식인 경우
        if visited[child] == 0:
            # 자식 계산
            func(child)
            memo[root][True] += min(memo[child][True], memo[child][False])
            memo[root][False] += memo[child][True]


N = int(sys.stdin.readline())
edge = [[] for _ in range(N + 1)]
memo = [[0, 0] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    V, W = map(int, sys.stdin.readline().split())
    edge[V].append(W)
    edge[W].append(V)

func(1)
print(min(memo[1][True], memo[1][False]))
