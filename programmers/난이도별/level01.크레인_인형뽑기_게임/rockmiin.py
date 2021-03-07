def solution(board, moves):
    basket= []
    n= len(board)
    cnt= 0
    for pick in moves:
        tmp= 0
        for idx in range(n):
            if board[idx][pick-1]!= 0:
                tmp= board[idx][pick-1]
                board[idx][pick-1]= 0
                break

        if tmp==0: continue

        if len(basket)>=1 and basket[-1]== tmp:
            basket.pop(-1); cnt+=2; continue
        basket.append(tmp)
    return cnt

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
         [1,5,3,5,1,2,1,4])