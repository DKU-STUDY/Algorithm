def solution(scoville, K):
    answer = 0
    s = sorted(scoville)
    while 1:
        if s[0] >= K:
            return answer
        if len(s) < 2:
            return -1
        # s가 가장 작은 s[0]가 K보다 작고 하나일 경우는 실패
        tmp = s.pop(0) + s.pop(0)*2
        # 가장 작은 것과 두 번째로 작은 것이 반환된 후 제거됨.
        answer += 1
        cnt = 0 # tmp가 s의 모든 요소 보다 큰 경우는 마지막 요소가 될 수 있게 하기 위해서
        for i, c in enumerate(s):
            if tmp < c:
                s.insert(i, tmp)
                cnt = 1
                break
        if cnt == 0:
            s.append(tmp)

print(solution([1, 2, 3, 9, 10, 12], 7) == 2)
