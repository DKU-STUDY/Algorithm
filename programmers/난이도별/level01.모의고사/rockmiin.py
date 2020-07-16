def solution(answers):
    m1=[]; m2=[]; m3=[]
    cnt=[0, 0, 0]
    ret_value=[]
    for i in range(1, len(answers)+1):
        if i%5==0: #수포자1
            m1.append(5)
        else: m1.append(i%5)

        if i%2==1: #수포자2
            m2.append(2)
        elif i%8==2:
            m2.append(1)
        elif i%8==4:
            m2.append(3)
        elif i%8==6:
            m2.append(4)
        elif i%8==0:
            m2.append(5)

        if i % 10 == 9 or i % 10 == 0: #수포자3
            m3.append(5)
        elif i%10<=2:
            m3.append(3)
        elif i%10<=4:
            m3.append(1)
        elif i%10<=6:
            m3.append(2)
        elif i%10<=8:
            m3.append(4)

    for i, j in enumerate(answers):
        if j == m1[i]:
            cnt[0]+=1
        if j == m2[i]:
            cnt[1]+=1
        if j == m3[i]:
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

