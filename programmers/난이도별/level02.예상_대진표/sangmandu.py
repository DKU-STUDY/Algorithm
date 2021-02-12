'''
https://programmers.co.kr/learn/courses/30/lessons/12985
예상 대진표
2의 제곱승 이용
'''

import math
def solution(n,a,b):
    m = int(math.log2(n))
    for i in range(1, m+1):
        if (a-1) // (2 ** i) == (b-1) // (2 ** i):
            return i


'''
이진수 문제는 비트연산자를 이용하는 것이 확실히 간단한 것 같다.
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()      
'''