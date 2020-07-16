def solution(answers):
    cnt=[0, 0, 0]
    ret_value=[]
    m1=[1, 2, 3, 4, 5]
    m2=[2, 1, 2, 3, 2, 4, 2, 5]
    m3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, j in enumerate(answers):
        if answers[i] == m1[i%5]:
            cnt[0]+=1
        if answers[i] == m2[i%8]:
            cnt[1]+=1
        if answers[i] == m3[i%10]:
            cnt[2]+=1

    for i in range(3):
        if max(cnt)==cnt[i]:
            ret_value.append(i+1)

    return ret_value


print(
    solution([1, 3, 2, 4, 2]),
    solution([1, 3, 2, 4, 2])==[1,2,3],
    solution([1,2,3,4,5]),
    solution([1,2,3,4,5])==[1]
)

