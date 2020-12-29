"""
시간 제한	                메모리 제한	제출	    정답	    맞은 사람	정답 비율
0.5 초 (추가 시간 없음)	128 MB	    29712	7434	5526	25.347%
문제
    자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
    첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

출력
    첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
"""
import sys

sys.setrecursionlimit(100000)


def sol():
    A, B, C = map(int, sys.stdin.readline().split())
    result = power(A, B, C)
    return result


def power(A, B, C):
    if B == 1:
        return A % C
    temp = power(A, B // 2, C)
    if B % 2 == 1:
        return temp * temp * A % C
    return temp * temp % C


print(sol())
