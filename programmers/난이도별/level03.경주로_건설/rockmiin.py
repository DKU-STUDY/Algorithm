from collections import deque

moves = [[0, 1, 'R'], [0, -1, 'L'], [1, 0, 'D'], [-1, 0, 'U']]

def solution(board):
    n = len(board[0])
    result = []

    def bfs(v):
        cost = [[0] * n for _ in range(n)]
        q = deque([v])
        cost[v[0]][v[1]] = 1
        while q:
            x, y, c, d = q.popleft()

            if x == n - 1 and y == n - 1:
                result.append(cost[x][y])
                continue;

            for dx, dy, dir in moves:
                tx, ty = x + dx, y + dy
                if 0 <= tx < n and 0 <= ty < n and board[tx][ty] == 0:
                    if d in ['L', 'R']:
                        if dir in ['L', 'R']:
                                new_cost = c+ 100
                        else:
                                new_cost = c+ 600
                    else:
                        if dir in ['L', 'R']:
                                new_cost = c+ 600
                        else:
                                new_cost = c+ 100

                    if not cost[tx][ty] or cost[tx][ty] > new_cost:
                        cost[tx][ty]= new_cost
                        q.append([tx, ty, new_cost,dir])

    # 처음 시작 방향에 따른 값 변경
    bfs([0, 0, 0, 'R'])
    bfs([0, 0, 0, 'D'])

    return min(result)


print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],
          [0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))