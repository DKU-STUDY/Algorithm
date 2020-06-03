def solution(priorities, location):
    temp = []
    for i in range(len(priorities)):
        temp += [[i,priorities[i]]]

    while temp[0][1] != max(priorities):
        for i in range(1,len(priorities)):
            if temp[0][1] < temp[i][1]:
                temp.append(temp[0][1])
                temp.remove(temp[0][1])

    for i in temp:
        if i[0] == location:
            return temp.index(i) + 1
            
# 시간초과 실패
