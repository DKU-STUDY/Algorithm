'''
https://programmers.co.kr/learn/courses/30/lessons/68935
10 -> 3 -> reverse -> 10
진법 원리를 이용해 앞뒤반전으로 바로 리스트 생성
'''

def solution(n):
    answer = ''
    while n != 0:
        answer += str(divmod(n, 3)[1])
        n //= 3
    return int(answer, 3)