'''
https://programmers.co.kr/learn/courses/30/lessons/76501
음양 더하기
'''

def solution(absolutes, signs):
    return sum([num*(2*int(sign)-1) for num, sign in zip(absolutes, signs)])

'''
오랜만에 알고리즘
다시 시작!
'''