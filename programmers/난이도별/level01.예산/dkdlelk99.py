def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i
        answer += 1
        if budget < 0:
            answer -= 1
            break
    return answer

print(solution([2,3,1,5,4],9) == 3)
print(solution([2,3,2,3],10) == 4)
