'''
https://programmers.co.kr/learn/courses/30/lessons/42583
124 나라의 숫자
[풀이]
1. 1 2 4의 3진법으로 10진수 표현하기
2. 나머지에 대하여 역순으로 4, 1, 2 매칭하기.
=> 이 때, 3의 배수에 대해서는 인덱스를 1씩 줄여줄 것.
'''
def solution(n):
    numbers = ['4', '1', '2']
    answer = ''
    while n:
        answer = numbers[n % 3] + answer
        n = n // 3 - (n % 3 == 0)
    return answer
'''
'''