import collections


def solution(board):
    answer = 0
    
    #y, x
    #초기 상태 / 검사 필요 X 한변이 최소 5이므로.
    Q = collections.deque([((0, 0),(0, 0 + 1))])
    discovered = set()
    discovered.add(((0, 0),(0, 0 + 1)))
    N = len(board) - 1
    
    def is_valid(pos):
        y, x = pos
        return 0 <= y <= N and 0 <= x <= N and board[y][x] == 0
    
    def move(npos1,npos2):
        if is_valid(npos1) and is_valid(npos2) and (npos1,npos2) not in discovered:
            Q.append((npos1,npos2))
            discovered.add((npos1,npos2))
        
    def is_answer(pos1,pos2):
        return pos1 == (N,N) or pos2 == (N,N)
    
    while Q:
        #이동 시작
        answer += 1
        for _ in range(len(Q)):
            #왼쪽, 오른쪽
            #위쪽, 아래쪽
            pos1, pos2 = Q.popleft()
            if is_answer(pos1,pos2):
                return answer - 1

            y1, x1 = pos1
            y2, x2 = pos2
            
            #이동
            #상하좌우로 움직인다.
            for dy, dx in (-1,0), (+1,0), (0,-1), (0,+1):
                npos1, npos2 = (y1 + dy, x1 + dx), (y2 + dy, x2 + dx)
                # 유효한 경우 이동한다.
                move(npos1,npos2)
            #회전한다.
            #가로형일때
            #y1, x1은 pos1
            #y2, x2는 pos2을 뜻한다.
            if y1 == y2:
                # a    b
                # pos1 pos2
                # c    d
                a = (y1-1,x1)
                b = (y2-1,x2)
                c = (y1+1,x1)
                d = (y2+1,x2)
                
                #왼쪽축을 기준으로 돌린다.
                #반시계로
                if is_valid(b):
                    move(a,pos1)
                     
                #시계로
                if is_valid(d):
                    move(pos1,c)
                
                #오른쪽을 기준으로 돌린다.
                #시계로
                if is_valid(a):
                    move(b,pos2)
                
                #반시계로
                if is_valid(c):
                    move(pos2,d)
                
            #세로형일때
            else:
                #
                #a pos1 b
                #c pos2 d
                a = (y1,x1-1)
                b = (y1,x1+1)
                c = (y2,x2-1)
                d = (y2,x2+1)
                
                #위축을 기준으로 돌린다.
                #반시계로
                if is_valid(c):
                    move(a,pos1)
                
                #시계로
                if is_valid(d):
                    move(pos1,b)
                
                #아래축을 기준으로 돌린다.
                #반시계로
                if is_valid(a):
                    move(c,pos2)
                #시계로
                if is_valid(b):
                    move(pos2,d)
    #모든 경우가 반드시 도착하는 경우가 있으므로 여기 도달할리는 없음.
    return -1