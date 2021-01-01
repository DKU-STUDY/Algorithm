from collections import deque
import sys

def bfs(v):

    q= deque([v])
    # print(v)
    while q:
        x, y= q.popleft()

        tmp= [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        for tmp_x, tmp_y in tmp:
            dx, dy= x+tmp_x, y+tmp_y
            if 0<=dx<h and 0<=dy<w and arr[dx][dy] and not visited[dx][dy]:
                q.append([dx, dy])
                visited[dx][dy] = 1 # append를 할 때 방문 처리를 해줘야 중복이 발생 x


while True:
    w, h= map(int, sys.stdin.readline().split())

    if w == 0 and h == 0: break;

    cnt = 0
    arr= []
    visited=[[0]* w for _ in range(h)]

    for i in range(h):
        arr.append(list(map(int, sys.stdin.readline().split())))
    # print(arr)

    for i in range(h):
        for j in range(w):
            if arr[i][j]==1 and visited[i][j]==0:
                bfs([i, j])
                cnt+=1
                # for k in range(h):
                #     print(visited[k])
                # print()
    print(cnt)