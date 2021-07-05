from collections import Counter
import heapq

def solution(n, works):
    answer = 0
    
    queue = []
    
    for idx, work in enumerate(works):
        heapq.heappush(queue, (-work,idx))
    
    for _ in range(n):
        value, idx = heapq.heappop(queue)
        if value == 0:
            return 0
        heapq.heappush(queue, (value + 1, idx))
    
    return sum([value**2 for value, idx in queue])