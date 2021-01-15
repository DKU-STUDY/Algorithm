'''
https://programmers.co.kr/learn/courses/30/lessons/12911
다음 큰 숫자
'''

def solution(n):
    one = format(n, 'b').count('1')
    while True:
        n += 1
        if one == format(n, 'b').count('1'): return n

'''
'''