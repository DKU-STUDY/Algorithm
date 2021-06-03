# 링크 : https://programmers.co.kr/learn/courses/30/lessons/42748
# 문제이름 : K번째 수

def solution(array, commands):
    answer = []
    temp_array = []
    size = len(commands)
    for i in range(0,size):
        for j in range(commands[i][0]-1, commands[i][1]) :
            temp_array.append(array[j])
        temp_array.sort()
        print(temp_array)
        answer.append(temp_array[commands[i][2]-1])
        temp_array.clear()
    return answer
