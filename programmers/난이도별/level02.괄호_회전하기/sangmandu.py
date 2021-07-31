'''
https://programmers.co.kr/learn/courses/30/lessons/76502
괄호 회전하기
[풀이]
1. 문자열 함수 replace 사용
'''
def solution(s):
    answer = 0
    for i in range(len(s)):
        brt = s[i:] + s[:i]
        temp = ''
        while temp != brt:
            temp = brt
            brt = brt.replace('[]','').replace('{}','').replace('()','')
        if len(brt) == 0:
            answer += 1
    return answer
'''
완벽하게 푼듯 하다
'''