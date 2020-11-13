def solution(citations):
    a = []
    for h in range(max(citations)):
        cnt = 0 # 논문 개수
        for nonmun in citations:
            if nonmun >= h:
                cnt += 1
        a.append(h)
        if cnt < h:
            return a[h - 1]
    return 0

print(solution([3, 0, 6, 1, 5]), solution([3, 0, 6, 1, 5]) == 3)
