'''
https://programmers.co.kr/learn/courses/30/lessons/12953
N개의 최소공배수
[풀이]
1. GCD 사용
'''
from math import gcd
def solution(arr):
    a = arr[0]
    for b in arr[1:]:
        a = a * b // gcd(a, b)
    return a
'''
'''