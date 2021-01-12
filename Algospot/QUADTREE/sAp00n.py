# 알고스팟 https://www.algospot.com/judge/problem/read/QUADTREE

"""
최대 2^20 * 2^20 크기의 픽셀을 가진 쿼드 트리로 압축된 이미지를
상하로 반전된 이미지를 쿼드트리로 압축시켜 출력하는 문제입니다.

n = 테스트케이스의 수이고
이후 n개의 줄에 걸쳐 압축된 이미지가 문자열로서 입력됩니다.
"""


from sys import stdin
from collections import deque


def count_ele(case):
    ele = case.popleft()
    if ele != 'x':
        return ele
    return [count_ele(case), count_ele(case), count_ele(case), count_ele(case)]


def reverse_case(section):
    if len(section) == 1:
        return str(section)
    return 'x' + reverse_case(section[2]) + reverse_case(section[3]) + reverse_case(section[0]) + reverse_case(section[1])


n = int(stdin.readline())
test_case = [deque(stdin.readline().strip('\n')) for i in range(n)]
for case in test_case:
    section = count_ele(case)
    print(reverse_case(section))