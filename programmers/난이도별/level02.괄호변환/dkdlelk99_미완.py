# 출처 https://programmers.co.kr/learn/courses/30/lessons/60058
# input '(' 또는 ')'으로만 이루어진 문자열 p, '('와 ')'의 개수는 항상 같다.
# output p를 올바른 괄호 문자열로 변환한 결과
def check(s):
    a =''
    for i in s:
        a += i
        if a[-2:] == '()':
            a = a[:-2]
    return True if a == '' else False

def solution(p):
    answer = ''
    if p == '':
        return ''  #1단계
    u = ''
    ch = 0
    for i in p:
        u += i
        ch = ch + 1 if i == '(' else ch - 1
        if ch == 0:
            break
    v = p[len(u):] # 여기까지 2단계

    if check(u):
        answer = u + solution(v)
    else:
        v = '(' + v
        solution(v)
        v += ')'
        u = u[-2:0:-1]

    return v

print(solution('))((()'), solution(')('))
