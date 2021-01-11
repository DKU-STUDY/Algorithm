# 출처 https://programmers.co.kr/learn/courses/30/lessons/12909
# input '(' 또는 ')'으로만 이루어진 문자열 s
# output 올바른 괄호인지 아닌지에 대한 bool 값

def solution(s):
    a =''
    if s.count('(') == s.count(')'):
        for i in s:
            a += i
            if a[-2:] == '()':
                a = a[:-2]
        return True if a == '' else False
    else:
         return False

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
