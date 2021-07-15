'''
https://programmers.co.kr/learn/courses/30/lessons/12912
두 정수 사이의 합
[풀이]
1. 간단한 수학적 공식 이용 : n(n+1)/2
'''
def solution(a, b):
    return (a+b)*(abs(a-b)+1)//2
'''
'''
