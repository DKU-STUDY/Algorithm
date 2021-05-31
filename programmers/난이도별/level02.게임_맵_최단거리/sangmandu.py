'''
https://programmers.co.kr/learn/courses/30/lessons/1844
게임 맵 최단거리
BFS 문제.
'''
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    stack = [(0, 0, 1)] # 현재 있는곳도 카운트
    save = []
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while True:
        if not stack:
            if not save:
                return -1
            stack, save = save, stack
        y, x, cost = stack.pop()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == 1 or maps[ny][nx] > cost + 1: # 첫 방문 또는 현재 방문이 저비용
                    maps[ny][nx] = cost + 1
                    if ny == n - 1 and nx == m - 1:
                        return cost + 1
                    save.append((ny, nx, cost + 1))
'''
from collections import deque

다음에는 컬렉션 디큐... 를 써봐야 겠다.
매일 stack, save가 습관이 되버려서..

또, visited를 쓸 수 있지만
map 자체에 마킹을 해서 최단거리를 가는 방법도 많이 써봐야 겠다
bfs 방식이라 가능한 것 같다.
'''