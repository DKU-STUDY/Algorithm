from collections import deque
n, m=map(int, input().split())
arr=[[] for _ in range(n+1)]
count=[]

def bfs(v):
    q=deque([v])
    cnt=0
    while q:
        k=q.popleft()
        if not visited[k]:
            visited[k]=1
            cnt += 1
            for e in arr[k]:
                q.append(e);
    count.append(cnt)

for i in range(m):
    x, y=map(int, input().split())
    arr[y].append(x)

for e in arr:
    e.sort()

for i in range(1, n+1):
    visited = [0 for _ in range(n + 1)]
    bfs(i)
for i in range(len(count)):
    if max(count)==count[i]:
        print(i+1, end=" ")
