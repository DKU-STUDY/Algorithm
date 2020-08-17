def solution(n, lost, reserve):
    inter=set(lost)&set(reserve); lost=set(lost)-inter; reserve=set(reserve)-inter
    for res in reserve:
        if res-1 in lost : lost.remove(res-1)
        elif res+1 in lost : lost.remove(res+1)
    return n-len(lost)
#100점
print(solution(5,[2,4],[1,3,5])==5)
print(solution(5,[2,4],[3])==4)


