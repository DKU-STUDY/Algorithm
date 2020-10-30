'''
https://programmers.co.kr/learn/courses/30/lessons/12940
최대공약수와 최소공배수
math.gcd
'''

from math import gcd
def solution(n, m):
    g = gcd(n, m)
    return [g, n*m//g]

'''
다음은 유클리드 호제법
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer
'''