'''
https://programmers.co.kr/learn/courses/30/lessons/64061
크레이 인형뽑기 게임
[풀이]
1. 각 열마다 있는 인형 개수 조사
2. movee에 대해 반복문
=> 뽑을 인형이 없으면 continue
=> 뽑을 인형이 있으면 bucket에 담고 top과 같은지 비교
=> 같으면 bomb 추가
3. 뽑은 인형은 bucket에 닮기고 top을 bucket에 마지막 원소로 지정
'''
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
'''
'''