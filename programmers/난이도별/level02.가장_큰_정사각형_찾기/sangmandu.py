'''
https://programmers.co.kr/learn/courses/30/lessons/12905
가장 큰 정사각형 찾기
'''

def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
    return max(board[i][j] for j in range(len(board[0])) for i in range(len(board))) ** 2

'''
'''