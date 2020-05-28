def solution(heights):
    answer = []
    for i in range(len(heights)-1,-1,-1):
        for j in range(i-1,-1,-1):
            # print(heights[j],' vs ',heights[i])
            if heights[j] > heights[i]:
                answer.append(j+1)
                break
        if j == 0:
            answer.append(0)
    answer.reverse()
    return answer
    
