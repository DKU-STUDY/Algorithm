def solution(numbers):
    answer = []
    size = len(numbers)
    for i in range(size-1):
        for j in range(i+1,size):
            answer.append(numbers[i] + numbers[j])
    
    return sorted(set(answer))