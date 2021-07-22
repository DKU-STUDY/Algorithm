'''
https://programmers.co.kr/learn/courses/30/lessons/62048
멀쩡한 사각형
1. 직사각형의 대각선을 지나는 1x1 격자 사각형 개수 구하기
2. 작은 길이가 1씩 증가할 때, 대각선을 지나는 격자 사각형의 개수는, 큰길이와 작은길이의 비가 정수일 때 1개, 정수가 아닐 때 2개
'''
from math import gcd
def solution(w,h):
    w, h = min(w, h), max(w, h)
    g = gcd(w, h)
    cnt, ele = h//g, h/w
    for i in range(1, w//g):
        if float(int(i * ele)) != i * ele: cnt += 1
    return w*h - cnt*g

'''
def solution(w,h):
    return w*h-w-h+gcd(w,h)
'''