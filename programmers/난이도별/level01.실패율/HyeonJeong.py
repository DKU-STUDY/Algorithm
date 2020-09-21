def solution(N, stages):
    answer = []
    nlist = []

    for j in range(0, N):
        nlist += [stages.count(j+1)/sum([1 if j <= s-1 else 0 for s in stages])]
        #stages는 1부터 시작하지만 failure 리스트는 0부터 시작하므로 s-1

    for j in range(N):
        m = max(nlist)
        if m == -1: break
        for i in range(N): #앞에서부터 for문이 돌아서 작은 번호의 스테이지가 먼저 오게 됨
            if nlist[i] == m:
                answer += [i+1]
                nlist[i] = -1
                break
    return answer

print(
    solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3,4,2,1,5],
    solution(4, [4,4,4,4,4]) == [4,1,2,3]
)