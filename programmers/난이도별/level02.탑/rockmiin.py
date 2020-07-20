def solution(heights):
    answer=[]
    slen=len(heights)
    heights.reverse()
    for i in range(slen):
        for j in range(i+1, slen):
            if heights[i] < heights[j] :
                answer.append(j); break;
        if i+1 != len(answer):
            answer.append(0)
    answer.reverse()

    for i in range(slen):
        if answer[i]!=0:
            answer[i]=slen-answer[i]
    return answer

print(
    solution([6, 9, 5, 7, 4]),
    solution([6, 9, 5, 7, 4])==[0, 0, 2, 2, 4]
)
