def solution(scoville, K):
    answer = 0
    s = sorted(scoville)
    while 1:
        if s[0] >= K:
            return answer
        if len(s) < 2:
            return -1
        tmp = s.pop(0) + s.pop(0)*2
        answer += 1
        cnt = 0
        for i, c in enumerate(s):
            if tmp < c:
                s.insert(i, tmp)
                cnt = 1
                break
        if cnt == 0:
            s.append(tmp)

print(solution([1, 2, 3, 9, 10, 12], 7) == 2)
