'''
https://programmers.co.kr/learn/courses/30/lessons/77485
행렬 테두리 회전하기
matrix 조작
'''
def solution(rows, columns, queries):
    answer = []
    board = [[row * columns + column + 1 for column in range(columns)] for row in range(rows)]
    for query in queries:
        y1, x1, y2, x2 = map(lambda a: a - 1, query)
        tmp = board[y1][x1]
        lst = [tmp]
        for x in range(x1 + 1, x2 + 1):
            board[y1][x], tmp = tmp, board[y1][x]
            lst.append(tmp)
        for y in range(y1 + 1, y2 + 1):
            board[y][x2], tmp = tmp, board[y][x2]
            lst.append(tmp)
        for x in range(x2 - 1, x1 - 1, -1):
            board[y2][x], tmp = tmp, board[y2][x]
            lst.append(tmp)
        for y in range(y2 - 1, y1 - 1, -1):
            board[y][x1], tmp = tmp, board[y][x1]
            lst.append(tmp)
        answer.append(min(lst))

    return answer
'''
나름 깔끔히 푼 것 같다
'''