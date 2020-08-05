def solution(prices):
    period = []
    for i in range(len(prices)) :
        state=False
        for j in range(i+1,len(prices)) :
            if prices[i]>prices[j] :
                period.append(j-i)
                state=True
                break
        if state==False :
            period.append(len(prices)-i-1)
    return period

print(solution([1,2,3,2,3])==[4,3,1,1,0])
#100점
