'''
https://programmers.co.kr/learn/courses/30/lessons/67259
경주로 건설
[풀이]
0. 문제에 오류가 있습니다.
https://programmers.co.kr/questions/18816
1. [0, 0] 에서 시작하는 dfs(bfs여도 상관없음)
2. 각 노드가 visited를 가지면 시간초과
=> 따라서 baord의 원소들이 최소 cost값을 비교해서 가지도록 함
=> DP 문제
3. 방향이 같으면 100, 코너가 생성되면 600
4. 마지막 좌표값을 반환
'''
def solution(board):
    stack = [[0, 0, 'START']] # y, x, direction
    size = len(board)
    board[0][0] = -500
    while stack:
        y, x, direction = stack.pop()
        cost = board[y][x]
        for dy, dx, drt in [(-1, 0, 'U'), (0, -1, 'L'), (1, 0, 'D'), (0, 1, 'R',)]:
            ny, nx = y + dy, x + dx
            c = 0
            if 0 <= ny < size and 0 <= nx < size:
                if board[ny][nx] != 1:
                    c += 100
                    if direction != drt:
                        c += 500
                    if board[ny][nx] == 0 or board[ny][nx] >= cost + c:
                        board[ny][nx] = cost+c
                        stack.append([ny, nx, drt])

    return board[-1][-1]
'''
문제에 오류가 있어서, 다르게 풀어보고 싶었는데 풀지 못했다.
'''