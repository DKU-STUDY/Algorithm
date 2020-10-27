'''
https://programmers.co.kr/learn/courses/30/lessons/12910
문자열 내림차순으로 배치하기
join, sorted, reverse option
'''

def solution(s):
    return ''.join(sorted(s, reverse=True))

'''
'''