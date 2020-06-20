def solution(answers):
    # 1번 12345
    # 2번 2 1 2 3 2 4 2 5  8개 반복
    # 3번 33 11 22 44 55  10개 반복
    answer_1 = [1,2,3,4,5]
    answer_2 = [2,1,2,3,2,4,2,5]
    answer_3 = [3,3,1,1,2,2,4,4,5,5]
    a, b, c = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == answer_1[i%5]:
            a += 1
        if answers[i] == answer_2[i%8]:
            b += 1
        if answers[i] == answer_3[i%10]:
            c += 1
    temp = [[a,1],[b,2],[c,3]]
    temp = sorted(temp, reverse = True)
    answer = [temp[0][1]]
    if temp[1][0] == temp[0][0]:
        answer.append(temp[1][1])
        if temp[2][0] == temp[0][0]:
            answer.append(temp[2][1])
    return sorted(answer)

print(solution([1, 2, 3, 4, 5]) == [1] )
print(solution([1, 3, 2, 4, 2]) == [1, 2, 3] )
