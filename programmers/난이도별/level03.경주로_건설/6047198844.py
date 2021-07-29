import heapq


def solution(board):
    answer = 0
    
    PQ = []
    heapq.heappush(PQ,((0,(0,0),'R')))
    heapq.heappush(PQ,((0,(0,0),'D')))
    
    N = len(board)
    visited = set()
    visited.add(((0,0),'R'))
    visited.add(((0,0),'D'))
    
    DICT = {'L':(0,-1), 'R':(0,1), 'U':(-1,0), 'D':(1,0)}
    route = [[0 for j in range(N)] for i in range(N)]
    
    while PQ:
        cost, pos, prev = heapq.heappop(PQ)
        for direction in 'L', 'R', 'U', 'D':
            y, x = pos
            dy, dx = DICT[direction]
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != 1:
            #and ((ny,nx),direction) not in visited:
                ncost = cost + 100
                if prev != direction:
                    ncost = cost + 600
                    
                if ((ny,nx),direction) not in visited or ncost < route[ny][nx]:
                    heapq.heappush(PQ,(ncost,(ny, nx),direction))
                    visited.add(((ny,nx),direction))
                    if route[ny][nx] == 0 or ncost < route[ny][nx]:
                        route[ny][nx] = ncost
    
    return route[N-1][N-1]