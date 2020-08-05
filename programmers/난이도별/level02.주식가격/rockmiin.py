def solution(prices):
    answer=[]
    for i in range(len(prices)):
        cnt=0
        for j in range(i+1, len(prices)):
            cnt+=1
            if prices[j]<prices[i]:
                break
        answer.append(cnt)
    return answer

print(
    solution([1, 2, 3, 2, 3])==[4, 3, 1, 1, 0]
)
