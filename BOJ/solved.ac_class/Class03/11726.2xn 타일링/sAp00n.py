# https://www.acmicpc.net/problem/11726

"""
시간 제한	    메모리 제한	제출	    정답	    맞은 사람	    정답 비율
1 초	    256 MB	    67991	25075	18388	    34.633%

문제
    2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

입력
    첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
    첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
"""
# 제대로 코드 짯는데 뎁스 터져버리는 경험은 처음이였다.
# 다행이 이전에 최대 깊이 수정하는 방법을 알아둬서 그걸로 풀이 완료.
# 재귀적으로 구현하면 생각이 편해져서 좋긴 한데, 다른 방법으로 풀이하는것도 연습해야할꺼같다.

import sys
sys.setrecursionlimit(2000)

def sol():
    n = int(sys.stdin.readline())
    global memo
    memo = {0: 0, 1: 1, 2: 2}
    print(cal(n) % 10007)


def cal(n):
    global memo
    if n in memo:
        return memo[n]
    else:
        memo[n] = cal(n - 1) + cal(n - 2)
        return memo[n]


sol()
