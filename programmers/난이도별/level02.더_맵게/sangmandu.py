'''
https://programmers.co.kr/learn/courses/30/lessons/42626
더 맵게
[풀이]
1. 가장 작은 2개의 원소에 대해 특정 연산 후 조건 확인
2. heapq 사용으로 매번 작은 수를 얻음
'''
import heapq as h
def solution(scoville, K):
    s = scoville[:]
    h.heapify(s)
    m1, m2 = h.heappop(s), h.heappop(s)
    if m1 == m2 == 0: return -1
    while True:
        h.heappush(s, m1+2*m2)
        if s[0] >= K: break
        if len(s) < 2: return -1
        m1, m2 = h.heappop(s), h.heappop(s)
    return len(scoville) - len(s)
'''
'''