def solution(rows, columns, queries):
    answer = []
    
    # 1 + (row - 1) * columns ~ row * columns
    board = [list(range(1 + (row - 1) * columns, row * columns + 1)) for row in range(1, rows+1)]
    
    for query in queries:
        top_y, top_x, bottom_y, bottom_x = query
        top_x -= 1
        top_y -= 1
        bottom_x -= 1
        bottom_y -= 1
        
        top = board[top_y][top_x:bottom_x]
        bottom = board[bottom_y][top_x+1:bottom_x+1]
        left = list(list(zip(*board))[top_x][top_y+1:bottom_y+1])
        right = list(list(zip(*board))[bottom_x][top_y:bottom_y])
        
        answer.append(min(top+bottom+left+right))
        
        #위쪽 이동
        for idx, x in enumerate(range(top_x+1, bottom_x+1)):
            board[top_y][x] = top[idx]
        
        #아래쪽 이동
        for idx, x in enumerate(range(top_x, bottom_x)):
            board[bottom_y][x] = bottom[idx]
        
        #왼쪽 이동
        for idx, y in enumerate(range(top_y, bottom_y)):
            board[y][top_x] = left[idx]
        
        #오른쪽 이동
        for idx, y in enumerate(range(top_y+1, bottom_y+1)):
            board[y][bottom_x] = right[idx]
            
    return answer