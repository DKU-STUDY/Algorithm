'''
https://programmers.co.kr/learn/courses/30/lessons/12900
2xn 타일링
n에 대한 각 값들이 피보나치 수열로 이루어져 있음
'''

def solution(n):
    a, b = 1, 2
    for i in range(3, n):
        a, b = b, a+b
    return (a+b) % 1000000007

'''
처음에 팩토리얼이나 콤비네이션으로 접근했는데,
결국 중복조합 문제인지라 내 지식선에서는 해결할 수 없었다.
n에 대한 각 값들이 피보나치 수열인지도 한참뒤에 알았음.
'''