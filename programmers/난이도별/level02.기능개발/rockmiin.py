import math
def solution(prograsses, speeds):
    slen=len(prograsses)
    days=[]
    cnt=[0] * slen
    answer=[]
    for i in range(slen):
        days.append(math.ceil((100-prograsses[i])/speeds[i]))
    for i in range(slen):
        tmp=sum(cnt)
        for j in range(i, slen):
            if days[i] < days[j]:
                break;
            cnt[j]=1
        if sum(cnt)-tmp!=0:
            answer.append(sum(cnt)-tmp)
    return answer

print(
    solution([93, 30, 55], [1, 30, 5]),
    solution([93, 30, 55], [1, 30, 5])==[2, 1]
)