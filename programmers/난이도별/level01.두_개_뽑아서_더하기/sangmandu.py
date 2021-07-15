'''
https://programmers.co.kr/learn/courses/30/lessons/68644
두 개 뽑아서 더하기
[풀이]
'''

def solution(numbers):
    answer = []
    size = len(numbers)
    for i in range(size-1):
        for j in range(i+1,size):
            answer.append(numbers[i] + numbers[j])
    
    return sorted(set(answer))
'''
'''