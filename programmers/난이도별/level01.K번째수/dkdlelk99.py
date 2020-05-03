def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        temp = array[commands[i][0] - 1 : commands[i][1] ]
        temp.sort()
        # print(temp)
        answer.append(temp[ commands[i][2] - 1 ])
    return answer
    
    
    
a = [[3, 3, 1], [3, 5, 2], [2, 7, 4]]
b =	[2, 3, 5, 4, 6, 1, 7, 9, 8]

# 함수 내부의 print문 결과
# [5]
# [4, 5, 6]
# [1, 3, 4, 5, 6, 7]

print(solution(b,a) == [5, 5, 5])
