'''
https://programmers.co.kr/learn/courses/30/lessons/49191
순위
[풀이]
1. 선수 번호는 1번부터 시작하므로 번호 - 1을 해서 그래프는 0번 부터 시작하도록 함
2. 이기면 1, 지면 -1을 할당
3. 어떤 선수 A가 이긴 사람 B가 있을 때 이긴 사람 B가 이긴 사람 C가 있다면 A가 C를 이긴다.
=> 각 선수에 대하여 반복문을 돌린다(첫번째 FOR). 이긴 사람 B를 찾는 과정
=> 그 선수가 이긴 선수에 대해서 또 반복문을 돌린다. 이긴 사람 C를 찾는 과정(두번째 FOR)
=> 이를 반복한다 (WHILE)
4. 정확하게 순위를 매길 수 있으려면 모든 선수와의 승패가 나타나져야 하므로 자신을 제외한 모든 숫자가 1 또는 -1
=> 따라서 count(0) == 1 이 되어야 한다.
'''
def solution(n, results):
    board = [[0] * n for _ in range(n)]
    for st, ed in results:
        board[st - 1][ed - 1] = 1
        board[ed - 1][st - 1] = -1

    for i in range(n):
        win = [idx for idx, val in enumerate(board[i]) if val == 1]
        while win:
            lose = win.pop()
            for idx, val in enumerate(board[lose]):
                if val == 1 and board[i][idx] == 0:
                    board[i][idx] = 1
                    board[idx][i] = -1
                    win.append(idx)

    return sum([i.count(0) == 1 for i in board])
'''
'''