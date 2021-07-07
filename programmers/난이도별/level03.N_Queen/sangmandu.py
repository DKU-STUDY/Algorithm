'''
https://programmers.co.kr/learn/courses/30/lessons/12952
N-Queen
[풀이]
1. stack에 다음과 같은 원소를 집어넣는다
{0} : story, 몇번째 가로줄인지.
=> 초기에 첫번째 가로줄로 초기화. 위에서부터 시작.
{1} : hor, 몇번째 세로줄을 고를 수 있는지.
=> 이전에 고른 세로줄은 고르지 못하므로 하나씩 없어진다.
=> 선택한 세로줄을 없애기 위해 set 자료형 선택
{2, 3} : diag1, diag2, 대각선 검사
=> 가장 왼쪽 위를 (1, 1) 이라고 하면
=> 기울기가 -1 인 대각선들의 공통점은 두 좌표의 차가 일정하다는 것 => diag1
=> 기울기가 1인 대각선들의 공통점은 두 좌표의 합이 일정하다는 것 => diag2
2. dfs 방식으로 조건을 만족할 때 마다 가로 층을 증가시키며 탐색한다.
=> bfs 방식이어도 큰 상관은 없음
'''
def solution(n):
    answer = 0
    stack = [[1, set(range(1, n + 1)), [], []]]
    while stack:
        story, hor, diag1, diag2 = stack.pop()
        if story == n + 1:
            answer += 1
            continue
        for x in hor:
            if x - story not in diag1 and x + story not in diag2:
                stack.append([story + 1, hor - set([x]), diag1 + [x - story], diag2 + [x + story]])

    return answer
'''
미친 풀이
nQueen = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184, 14772512, 95815104, 666090624, 4968057848, 39029188884,
314666222712, 2691008701644, 24233937684440, 227514171973736, 2207893435808352, 22317699616364044, 234907967154122528].__getitem__
'''