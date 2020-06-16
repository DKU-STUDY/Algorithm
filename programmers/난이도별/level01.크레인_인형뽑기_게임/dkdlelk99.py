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
            element = new_board[i-1].pop(0)
            if basket == []:
                basket.append(element)
            elif basket[-1] != element:
                basket.append(element)
            elif basket[-1] == element:
                answer += 1
                basket.remove(basket[-1])
    return answer*2
