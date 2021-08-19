'''
https://www.acmicpc.net/problem/7562
나이트의 이동
[풀이]
1. 방문 여부를 조사하는 visited 배열을 l * l 크기로 선언
2. BFS로 풀 것이므로 stack과 save 생성
=> 최단 거리를 구하는 문제기 때문에 BFS
3. 나이트가 이동할 수 있는 거리는 절댓값이 1과 2인 수의 조합이다.
'''
n = int(input())
for _ in range(n):
    l = int(input())
    y1, x1 = map(int, input().split())
    y2, x2 = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    visited[y1][x1] = 1
    stack, save = [(y1, x1, 0)], []
    while True:
        if not stack:
            stack, save = save, stack
        y, x, cnt = stack.pop()
        if y == y2 and x == x2:
            print(cnt)
            break
        for dy in [-2, -1, 1, 2]:
            for dx in [3-abs(dy), abs(dy)-3]:
                ny, nx = y+dy, x+dx
                if 0 <= ny < l and 0 <= nx < l and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    save.append((ny, nx, cnt+1))
