def solution(citations):
    a = []
    for h in range(len(citations)):
        answer = 0 # 논문 갯수
        for nonmun in citations:
            if nonmun >= h:
                answer += 1
        a.append(h)
        if answer < h:
            return a[h - 1]

print(solution([3, 0, 6, 1, 5]), solution([3, 0, 6, 1, 5]) == 3)
