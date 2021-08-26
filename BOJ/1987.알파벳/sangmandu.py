'''
https://www.acmicpc.net/problem/1987
알파벳
[풀이]
1. BFS로 풀이
=> 최대길이를 조사할 떄는 DFS보다 BFS가 더 유리하다고 한다
2. set으로 queue의 역할
3. 방문여부를 조사하면서 탐색 후 거리 세기
=> 이 떄의 방문여부는 좌표가 아니라 문자
'''
import sys
input = sys.stdin.readline
h, w = map(int, input().strip().split())
board = [input().strip() for _ in range(h)]
max_move = 1
q = set([(0, 0, board[0][0])])
while q:
    y, x, visited = q.pop()
    for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < h and 0 <= nx < w and board[ny][nx] not in visited:
            max_move = max(max_move, len(visited)+1)
            q.add((ny, nx, visited+board[ny][nx]))

print(max_move)