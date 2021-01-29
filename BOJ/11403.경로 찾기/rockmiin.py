from collections import deque

def bfs(start, end):
    visited= [0]*n

    if start== end:
        q= deque(adj[start])
        for i in adj[start]:
            visited[i]= 1

    else:
        q= deque([start])
        visited[start]= 1

    while q:
        v= q.popleft()

        if v== end:
            arr2[start][end]= 1; break;
        for val in adj[v]:
            if not visited[val]:
                q.append(val)
                visited[val]= 1

n= int(input())
arr= []
arr2= [[0]*n for _ in range(n)]
adj=[[] for _ in range(n)]
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if arr[i][j]== 1:
            adj[i].append(j)
# print(adj)
for i in range(n):
    for j in range(n):
        bfs(i, j)

for i in arr2:
    for j in i:
        print(j, end= " ")
    print()

# for i in arr2:
#     print(i)