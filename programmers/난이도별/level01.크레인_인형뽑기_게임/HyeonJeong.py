def solution(board, moves):
    answer = 0
    slist = []
    length = len(board)
    for m in moves:
        if board[length-1][m-1] == 0:
            continue
        for i in range(length):
            if board[i][m - 1] != 0:
                if len(slist) > 0 and slist[-1] == board[i][m - 1]:
                    answer += 2
                    slist.pop(-1)
                else:
                    slist.append(board[i][m - 1])
                board[i][m - 1] = 0
                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]) == 4)
