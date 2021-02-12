'''
https://leetcode.com/problems/regions-cut-by-slashes/
GRAPH : BFS 이용
한 개의 정사각형이 9개의 작은 정사각형으로 이루어져있다고 생각.
이 때 대각선을 그으면 BFS로 visited 여부 확인 가능
(4개의 정사각형은 대각선방향으로 있는 영역을 visited 여부 확인 불가)
'''

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        square = [[0] * N * 3 for _ in range(N * 3)]
        for j in range(N):
            for i in range(N):
                if grid[j][i] == ' ':
                    continue
                if grid[j][i] == '/':
                    for k in range(3):
                        square[j * 3 + k][i * 3 + 2 - k] = 1
                    continue
                if grid[j][i] == '\\':
                    for k in range(3):
                        square[j * 3 + k][i * 3 + k] = 1
                    continue

        def bfs(y, x):
            for ay, ax in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ny, nx = y + ay, x + ax
                if 0 <= ny < 3 * N and 0 <= nx < 3 * N and visited[ny][nx] == 0 and square[ny][nx] == 0:
                    visited[ny][nx] = 1
                    bfs(ny, nx)

        visited = [[0] * N * 3 for _ in range(N * 3)]
        cnt = 0
        for y in range(N * 3):
            for x in range(N * 3):
                if visited[y][x] == 0 and square[y][x] == 0:
                    visited[y][x] = 1
                    bfs(y, x)
                    cnt += 1

        return cnt

'''
코드 속도가 좀 느려서 아쉽.
'''