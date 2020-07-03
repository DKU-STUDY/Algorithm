def solution(board, moves):
    answer = 0
    basket = []
    new_board = []
    for i in range(len(board)):
        row = []
        for j in range(len(board)):
            if board[j][i] != 0:
                row.append(board[j][i])
        new_board.append(row)
    
    for i in moves:
        if new_board[i-1] == []:
            continue
        else:
            if basket == []:
                basket.append(new_board[i-1].pop(0))
                continue
            element = new_board[i-1].pop(0)
            if basket[-1] != element:
                basket.append(element)
            elif basket[-1] == element:
                answer += 2
                basket.pop()
    return answer

board = [[0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 2, 5, 0, 1],
        [4, 2, 4, 4, 2],
        [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves) == 4)
