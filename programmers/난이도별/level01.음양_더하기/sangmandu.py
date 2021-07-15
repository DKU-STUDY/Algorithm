'''
https://programmers.co.kr/learn/courses/30/lessons/76501
음양 더하기
[풀이]
'''
def solution(absolutes, signs):
    return sum([num*(2*int(sign)-1) for num, sign in zip(absolutes, signs)])
'''
'''