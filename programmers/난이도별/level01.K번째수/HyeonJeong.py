# 1. 첫 시도
'''
def solution(array, commands):
    answer = []
    for j in range(len(commands)) :
        new_array = []
        for i in range(commands[j][0] - 1, commands[j][1]) :
            new_array.append(array [i])
        new_array.sort()
        answer.append(new_array [(commands [j][2] - 1)])
    return answer
'''

# 2. list[:]이용
'''
def solution(array, commands):
    answer = []
    for j in range(len(commands)) :
        new_array =  array [commands[j][0] - 1 : commands[j][1]]
        new_array.sort()
        answer.append(new_array [(commands [j][2] - 1)])
    return answer
'''

# 3. sorted()이용
'''
def solution(array, commands):
    answer = []
    for j in range(len(commands)) :
        new_array =  sorted(array [commands[j][0] - 1 : commands[j][1]])
        answer.append(new_array [(commands [j][2] - 1)])
    return answer
'''

# 4. 더 짧은 코드 이용
'''
def solution(array, commands):
    answer = []
    for j in range(len(commands)) :
        answer.append(sorted(array [commands[j][0] - 1 : commands[j][1]])[(commands [j][2] - 1)])
    return answer
'''

# 5. 준일님의 코드 이용
def solution(array, commands):
    answer = []
    for x, y, z in commands :
        answer.append(sorted(array [x - 1 : y])[z - 1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
