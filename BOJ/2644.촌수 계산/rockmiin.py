from collections import deque

def bfs(start, end):
    q= deque([start])
    while q:
        v= q.popleft()

        if v== end: break;

        for i in adj[v]:
            if not visited[i]:
                q.append(i)
                visited[i]= visited[v]+1

    if visited[end]==0:
        return -1

    return visited[end]

n= int(input())
start, end= map(int, input().split())
m= int(input())

adj= [[] for _ in range(n+1)]

for i in range(1, m+1):
    x, y= map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for i in adj:
    i.sort()

# print(adj)

visited = [0 for _ in range(n + 1)]

print(bfs(start, end))

# idea
# 처음에 부모 -> 자식 일방향 탐색으로 생각을 했는데 노드에 양쪽으로 넣어 준 다음 간단하게 시작점과 끝점을 지정해줘서
# 그 위치에 도달하게 되면 bfs를 빠져나와 그 때의 촌 수를 출력해주면 됨
# 방문 여부와 촌 수를 같이 계산해주는 visited list를 사용하였음
# 방문을 하지 않았을 경우에는 즉 visited==0이라면 -1로 출력하는 예외 처리를 해줘야 함
