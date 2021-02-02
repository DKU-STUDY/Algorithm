# 뽑으려는 대상의 위치에 가서 0이 아닐 때까지 depth를 증가시켜서 뽑은 뒤 0으로 값을 바꿔주고
# 그 값이 basket 마지막에 있는 값과 같으면 사라지게 해주고 아니면 basket에 append하는 식으로 구현을 하였다.
# pick 위치에 아무것도 들어있지 않다면 continue를 해서 생략을 해주었다.

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