'''
https://programmers.co.kr/learn/courses/30/lessons/17679
프렌즈4블록
board를 만지기 쉽게 90도 회전함.
이후 자기 자신과 왼쪽 위, 왼쪽, 위가 같으면 0으로 변경. 이후, 0을 다 뺴고 그만큼 뒤에 다시 채워넣음.
'''

def solution(m, n, board):
    board = [list(e) for e in zip(*board[::-1])]
    while True:
        cnt = 0
        rid = []
        for i in range(1, n):
            for j in range(1, m):
                if board[i][j] and board[i][j] == board[i - 1][j] == board[i][j - 1] == board[i - 1][j - 1]:
                    rid.append((i, j))
                    cnt += 1
        if cnt == 0: break

        for i, j in rid:
            board[i][j] = board[i - 1][j] = board[i][j - 1] = board[i - 1][j - 1] = 0

        for i in board:
            while 0 in i:
                i.remove(0)
            while len(i) != m:
                i.append(0)

    return sum([i.count(0) for i in board])

'''     
'''