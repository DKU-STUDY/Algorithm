'''
괄호 변환
https://programmers.co.kr/learn/courses/30/lessons/60058
[풀이]
1. 문제에서 제시한 대로 풀이
'''
 def bracket(p):
    if len(p) == 0:
        return ''
    
    u = v = ""
    bal = 0
    for i in p:
        bal += 1 if i == "(" else -1
        u += i
        if bal == 0: 
            break
    v += p[len(u):]

    cnt = 0
    for i in u:    
        cnt += 1 if i == "(" else -1
        if cnt < 0:
            break
    
    if cnt == 0:
        return u + bracket(v)
    
    string = ""
    if cnt < 0 :
        string += "(" + bracket(v) + ")"
        for i in u[1:-1]:
            string += "(" if i == ")" else ")"
        return string
    
def solution(p):
    return bracket(p)
'''
'''