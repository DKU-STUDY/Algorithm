"""
시간 제한	                메모리 제한	제출	    정답	    맞은 사람	정답 비율
0.5 초 (추가 시간 없음)	128 MB	    50108	23747	17747	47.867%

문제
    RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

    집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때,
    아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

    1번 집의 색은 2번 집의 색과 같지 않아야 한다.
    N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
    i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
입력
    첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다.
    둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다.
    집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
    첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
"""

import sys

N = int(sys.stdin.readline())

cost_list = []
for _ in range(N):
    cost_list.append(tuple(map(int, sys.stdin.readline().split())))

result_list = [cost_list[0]]

for i in range(1, N):
    r_result = min(result_list[i - 1][1], result_list[i - 1][2]) + cost_list[i][0]
    g_result = min(result_list[i - 1][0], result_list[i - 1][2]) + cost_list[i][1]
    b_result = min(result_list[i - 1][0], result_list[i - 1][1]) + cost_list[i][2]
    result_list.append([r_result, g_result, b_result])

print(min(result_list[N - 1]))
