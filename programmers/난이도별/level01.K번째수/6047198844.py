def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i-1:j])[k-1])
        
    return answer