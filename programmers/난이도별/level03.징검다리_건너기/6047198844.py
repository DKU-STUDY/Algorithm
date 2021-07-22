import heapq
import collections

def solution(stones, k):
    window = collections.Counter(stones[:k])
    answer = max_value = max(window)
    
    #최대값추출하는곳
    heap = list(map(lambda key:-key, window.keys()))
    heapq.heapify(heap)
    stone_value = set(window.keys())
    
    begin = 0
    for end in range(k, len(stones)):
        #삭제할값
        i = stones[begin]
        begin += 1
        #추가할값
        j = stones[end]
        #윈도우 조정
        window[i] -= 1
        window[j] += 1
        stone_value.add(j)
        heapq.heappush(heap, -j)
        
        if window[i] == 0:
            del window[i]
            stone_value.remove(i)
        
        while -heap[0] not in stone_value:
            heapq.heappop(heap)
        
        answer = min(answer, -heap[0])
        #print(heap,answer,window)
    
    return answer