'''
https://programmers.co.kr/learn/courses/30/lessons/12909
올바른 괄호
'''

def solution(s):
    cnt = 0
    for i in s:
        if i == "(":
            cnt += 1
            continue
        cnt -= 1
        if cnt < 0: break
    return cnt == 0

'''
'''