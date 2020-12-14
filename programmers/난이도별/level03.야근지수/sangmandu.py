'''
https://programmers.co.kr/learn/courses/30/lessons/49994
야근지수
max heap 사용
'''

from heapq import heappush, heappop, heapify
def solution(n, works):
    works = [-i for i in works]
    heapify(works)
    for i in range(n):
        if works[0] == 0: return 0
        heappush(works, heappop(works) + 1)
    return sum([i*i for i in works])

'''
'''