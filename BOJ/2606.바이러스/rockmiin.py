from collections import deque

n= int(input())
m= int(input())

def bfs(v):
    q= deque([v])
    cnt= 0
    visited[v]=1
    while q:
        v= q.popleft()

        for i in arr[v]:
            if not visited[i]:
                q.append(i)
                visited[i]=1
        cnt+=1

    return cnt-1

arr=[[] for _ in range(n+1)]
# print(arr)

for i in range(m):
    x, y= map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

# 정점 크기 순서대로 정렬
for i in arr:
    i.sort()

visited=[0 for _ in range(n+1)]

print(bfs(1))

# 입력 예시
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

# 출력 4