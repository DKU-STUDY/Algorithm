from collections import deque

def bfs(v):
    q= deque([v])
    visited[v]= 1

    while q:
        x= q.popleft()

        if x== G: return visited[x]-1

        if x+U <= F and not visited[x+U]:
            # print("U", x+U)
            q.append(x+U)
            visited[x+U]= visited[x]+ 1
        if x-D >=1 and not visited[x-D]:
            # print("D", x-D)
            q.append(x-D)
            visited[x-D]= visited[x]+ 1
    return 'use the stairs'


F, S, G, U, D= map(int, input().split())
visited= [0]* (F+1)

print(bfs(S))

