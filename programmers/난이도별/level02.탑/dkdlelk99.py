def solution(heights):
    answer = []
    for i in range(len(heights)-1,-1,-1):
        check = False
        for j in range(i-1,-1,-1):
            if heights[j] > heights[i]:
                check = True
                answer.append(j+1)
                break
        if not check:
            answer.append(0)
    answer.reverse()
    return answer

print(solution([6,9,5,7,4]) == [0, 0, 2, 2, 4])
print(solution([3, 9, 9, 3, 5, 7, 2]) == [0, 0, 0, 3, 3, 3, 6])
print(solution([1, 5, 3, 6, 7, 6, 5]) == [0, 0, 2, 0, 0, 5, 6])
