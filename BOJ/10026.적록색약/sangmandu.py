'''
https://www.acmicpc.net/problem/10026
적록색약
[풀이]
1. 동일한 작업을 2번해야 한다
=> 전체 반복문을 2번 설정
=> cnt도 크기가 2인 배열로 설정
=> boards도 기존 board와 G또는 R중에 하나로 합쳐진 board 하나 선언
2. 상하좌우를 살피며 방문여부와 기준점과의 색 비교를 통해 cnt
'''
n = int(input())
board = [input() for _ in range(n)]
boards = [board, [color.replace('G', 'R') for color in board]]
cnt = [0, 0]
for idx in range(2):
    visited = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if visited[y][x]:
                continue
            stack = [(y, x)]
            cnt[idx] += 1
            while stack:
                b, a = stack.pop()
                for db, da in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nb, na = b+db, a+da
                    if 0 <= nb < n and 0 <= na < n:
                        if not visited[nb][na] and boards[idx][nb][na] == boards[idx][b][a]:
                            visited[nb][na] = 1
                            stack.append((nb, na))
print(*cnt)