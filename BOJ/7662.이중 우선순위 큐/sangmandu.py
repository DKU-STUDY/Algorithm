'''
https://www.acmicpc.net/problem/7662
이중 우선순위 큐 : minheap과 maxheap에서 pop하기
maxheap을 구현하는 대신, rid 리스트를 생성하여 결과 도출 시 예외해야 할 값들을 저장
'''
# Unsolved
from sys import stdin
import heapq as h

def solution(k):
    min_h = []
    rid = []
    for i in range(k):
        a, b = stdin.readline().split()
        if a == "I":
            h.heappush(min_h, (int(b), i))
            continue
        if len(min_h) == len(rid):
            continue
        if b == "-1":
            h.heappop(min_h)
        else:
            rid.append(sorted(list(min_h)).pop())
    if len(min_h) == len(rid):
        print("EMPTY")
    else:
        ret = list(set(min_h)-set(rid))
        ret.sort()
        print(ret[-1][0], ret[0][0])

T = int(stdin.readline())
for _ in range(T):
    k = int(stdin.readline())
    solution(k)

'''
'''