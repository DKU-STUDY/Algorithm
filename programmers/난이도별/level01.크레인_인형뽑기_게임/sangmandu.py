def solution(board, moves):
    numLine = [0 for i in range(len(board))]
    
    for i in board:
        for idx, val in enumerate(i):
            numLine[idx] += 1 if val != 0 else 0
    gameSize = len(numLine)        
    numLine.insert(0,0)
    #print(numLine, moves)
    
    bucket = []
    top =  bomb = 0
    for i in moves:
        #print("i : ", i, ", numLine[i] : ", numLine[i])
        if numLine[i] == 0:
            continue
        #print("top : ", top, ", board[gameSize-numLine[i]][i-1] : ", board[gameSize-numLine[i]][i-1])
        if top != board[gameSize-numLine[i]][i-1]:
            bucket.append(top)
            top = board[gameSize-numLine[i]][i-1]
            numLine[i] -= 1
            #print("bucket + top : ", bucket, top)
            continue
        top = bucket.pop()
        numLine[i] -= 1
        bomb += 1
        #print("bucket + top : ", bucket, top, ", bomb : ", bomb)
        
    return 2 * bomb