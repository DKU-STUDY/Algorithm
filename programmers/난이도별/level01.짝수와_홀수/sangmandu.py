'''
https://programmers.co.kr/learn/courses/30/lessons/12937
짝수와 홀수
%2
'''

def solution(num):
    return num % 2 and "Odd" or "Even"

'''
%2 대신 비트 연산자로 & 1 로 짝홀수 구분 가능
'''