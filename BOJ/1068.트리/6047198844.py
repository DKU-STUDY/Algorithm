N = int(input())
parents = list(map(int, input().split()))
edges = [[] for _ in range(N)]

for j in range(N):
    # j의 부모는 i 이다.
    i = parents[j]
    if i != -1:
        # 부모 -> 자식
        edges[i].append(j)
    else:
        root = j

def dfs(V):
    global res
    visited.add(V)


    cnt = 0
    # 방문할곳 있으면 방문
    for W in edges[V]:
        if W not in visited:
            cnt += 1
            dfs(W)

    # 방문을 하지 않았다면 리프노드
    if cnt == 0:
        res += 1

# 삭제 노드
di = int(input())
res = 0
# 루트 삭제의 경우 예외
if root != di:
    visited = set()
    visited.add(di)
    dfs(root)

print(res)
