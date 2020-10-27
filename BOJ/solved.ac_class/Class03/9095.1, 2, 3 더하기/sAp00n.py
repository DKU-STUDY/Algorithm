# https://www.acmicpc.net/problem/9095
"""
시간 제한	    메모리 제한	제출	    정답	    맞은 사람	    정답 비율
1 초	    128 MB	    50501	32144	21313	    61.645%

문제
    정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

        1+1+1+1
        1+1+2
        1+2+1
        2+1+1
        2+2
        1+3
        3+1
    정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
    첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

출력
    각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
"""

# 재귀로 간단하게 구현이 가능함. 풀고 보니 DP 문제였다고 한다

from sys import stdin


def compute(n):
    if n == 3:
        return 4
    if n == 2:
        return 2
    if n == 1:
        return 1
    return compute(n - 1) + compute(n - 2) + compute(n - 3)


def sol():
    n = int(stdin.readline())
    print(compute(n))


T = int(stdin.readline())

for _ in range(T):
    sol()
