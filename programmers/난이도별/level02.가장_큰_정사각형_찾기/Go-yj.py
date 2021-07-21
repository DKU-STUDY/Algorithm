'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12905#
문제 : 가장 큰 정사각형 찾기
진짜 엄청나게 헤맨 문제다. 사실 어떻게 풀어야 하는지 거의 외운 수준 같다.
왜 왼쪽이랑 위쪽이랑 대각선이랑 비교해서 min 값을 사용하는지 모르겠어서
설명하는 사이트를 많이 찾아봤지만 다들 푸는 방법만 알려주고 설명은 안해주고..ㄒ︿ㄒ
매번 DP 문제는 시간 오래걸리고 이해하기 어려운 듯..
DP 문제에 익숙해져야 겠다.
'''

def solution(board):
    answer = -1
    for i in range(1,len(board)) :
        for j in range(1,len(board[0])) :
            if board[i][j] == 1 :
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1])+1
                answer = max(answer, board[i][j])
    return answer**2 if answer !=-1 else board[0][0]
