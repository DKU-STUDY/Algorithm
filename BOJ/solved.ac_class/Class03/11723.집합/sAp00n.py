# https://www.acmicpc.net/problem/11723

"""
시간 제한	    메모리 제한	    제출	    정답	    맞은 사람	    정답 비율
1.5 초	    4 MB (하단 참고)	24904	7507	5181	    29.779%

문제
    비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

    add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    all: S를 {1, 2, ..., 20} 으로 바꾼다.
    empty: S를 공집합으로 바꾼다.

입력
    첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

    둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

출력
    check 연산이 주어질때마다, 결과를 출력한다.
"""

# 비트 마스킹으로 풀이.
# 다중 if문을 피할 수 있는 방법이 있었을까? => 함수 선언하여 캡슐화 해야했을지 고민
from sys import stdin

M = int(stdin.readline())

set = bin(1048576)
# print(set)

commend_list = ['add', 'remove', 'check', 'toggle', 'all', 'empty']

for _ in range(M):
    commend = stdin.readline().split()
    commend_idx = commend_list.index(commend[0])
    if commend_idx == 0:
        set = bin(int(set, 2) | (1 << int(commend[1])))
    elif commend_idx == 1:
        set = bin(int(set, 2) & ~(1 << int(commend[1])))
    elif commend_idx == 2:
        temp = int(bin(int(set, 2) & (1 << int(commend[1]))), 2)
        if temp > 0:
            print(1)
        else:
            print(0)
    elif commend_idx == 3:
        set = bin(int(set, 2) ^ (1 << int(commend[1])))
    elif commend_idx == 4:
        set = bin(2097151)
    else:
        set = bin(1048576)
