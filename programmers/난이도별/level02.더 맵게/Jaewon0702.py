import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    n=0
    while(len(scoville)>1) :
        state=False
        if scoville[0]<K :
            state=True
            heapq.heappush(scoville,heapq.heappop(scoville)+(heapq.heappop(scoville)*2))
            n+=1

        if state == False :
            break

    return -1 if scoville[0]<K else n

#100점
print(solution([1,2,3,9,10,12],7)==2)
