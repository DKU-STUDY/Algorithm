'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/77884
문제 : 약수의 개수와 덧셈
약수의 개수가 홀수일때는 제곱근이 정수일때이기 때문에 이를 판별하여 홀, 짝을 구해줬습니다.
'''

import math

def solution(left, right):
    answer = 0
    for i in range(left, right+1) :
        num = math.sqrt(i)
        if int(num) == num :
            answer -= i
        else : answer += i
    return answer
