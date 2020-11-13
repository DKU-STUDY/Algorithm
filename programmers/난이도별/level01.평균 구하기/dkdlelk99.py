def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    return answer/len(arr)


print(solution([1,2,3,4]) == 2.5)
print(solution([1,4,7,9]) == 5.25)
