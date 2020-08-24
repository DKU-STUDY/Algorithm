import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    
    while heap != []:
        if heap[0] >= K:
            return answer
        most_not_spicy = heapq.heappop(heap)
        if heap != []:
            heapq.heappush(heap, most_not_spicy + (2 * heapq.heappop(heap) ))
            answer += 1
    return -1 if heap == [] else answer

print(solution([1, 2, 3, 9, 10, 12], 7), solution([1, 2, 3, 9, 10, 12], 7) == 2)
