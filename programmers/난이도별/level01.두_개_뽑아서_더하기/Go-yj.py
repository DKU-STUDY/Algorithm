'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/68644
문제 : 두 개 뽑아서 더하기

'''

def solution(numbers):
    answer = []
    for i in range(len(numbers)) :
        for j in range(i+1, len(numbers)) :
            sum = numbers[i]+numbers[j]
            if sum not in answer : 
                answer.append(sum)
    answer.sort()
    return answer
