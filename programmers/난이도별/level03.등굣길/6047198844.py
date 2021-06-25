def solution(m, n, puddles):
    #board[y][x] : (y,x)에서 이동했을때의 경우의수
    board = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    board[n][m] = 1
    for x, y in puddles:
        board[y][x] = 0
    
    def dp(y, x):
        if not (1 <= y <= n and 1 <= x <= m):
            return 0
        if board[y][x] != -1:
            return board[y][x]
        
        board[y][x] = 0
        board[y][x] = ((dp(y+1,x) % 1000000007) + dp(y,x+1) % 1000000007) % 1000000007
        return board[y][x]    
    dp(1, 1)
    return board[1][1]