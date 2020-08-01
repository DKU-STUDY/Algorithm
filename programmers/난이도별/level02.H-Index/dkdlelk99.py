def solution(citations):
    for i in range(len(citations)):
        answer = 0
        for nonmun in citations:
            if nonmun >= i:
                answer += 1
        if answer == i:
            return answer

print(solution([3, 0, 6, 1, 5]), solution([3, 0, 6, 1, 5]) == 3)
