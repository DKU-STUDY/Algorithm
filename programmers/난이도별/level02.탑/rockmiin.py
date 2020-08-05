def solution(heights):

    slen=len(heights)
    answer=[0 for _ in range(slen)]
    for i in range(slen-1, 0, -1):
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j] :
                answer[i]=j+1; break;
    return answer

print(
    solution([6, 9, 5, 7, 4]),
    solution([6, 9, 5, 7, 4])==[0, 0, 2, 2, 4]
)
