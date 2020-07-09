import heapq

def solution(s, K):
    heapq.heapify(s)
    a = 0
    if s[0] >= K : return 0
    while len(s) > 1 :
        heapq.heappush(s, heapq.heappop(s) + heapq.heappop(s) * 2)
        a += 1
        if s[0] >= K : return a
    return -1
    
print(solution([1, 2, 3, 9, 10, 12], 100))
print(solution([1, 2], 7))
print(solution([1], 2))
print(solution([5], 5))
print(solution([1,2,7], 5))
print(solution([2,3,7], 7))
print(solution([0], 0))