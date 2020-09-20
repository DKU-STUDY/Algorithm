def solution(N, stages):
    answer = []
    nlist = []
    failure = [[0]*2 for i in range(N)]
    for j in range(0, N): #stages는 1부터 시작하지만 failure 리스트는 0부터 시작하므로 s-1
        for s in stages:
            if j <= s-1:
                failure[j][1] += 1
                if j == s-1:
                    failure[j][0] += 1

        if failure[j][1] == 0: #스테이지에 도달한 유저가 없는 경우에는 실패율 0
            nlist += [0]
            continue
        nlist += [failure[j][0]/failure[j][1]]

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