board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    basket = []
    board = [list(x) for x in zip(*board)]
    for move in moves:
        for idx in range(len(board[move-1])):
            if board[move-1][idx] != 0:
                basket.append(board[move-1][idx])
                board[move-1][idx] = 0
                break
    
    result = 0
    while(True):
        match = False
        for idx in range(len(basket)-1):
            if basket[idx] == basket[idx+1]:
                result += 1
                basket[idx] = 0
                basket[idx+1] = 0
                basket = basket[:idx] + basket[idx+2:]
                match = True
                break
        if not match:
            return result*2

print(solution(board, moves))