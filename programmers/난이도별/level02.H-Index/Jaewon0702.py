def solution(citations):
    citations.sort(reverse=True)
    for h in range(max(citations),-1,-1) :
        for cite in range(len(citations)) :
            if (citations[cite]>=h) :
                if (cite+1>=h) :
                    return h
                    break

#100점
