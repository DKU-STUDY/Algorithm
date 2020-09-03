import math

def solution(s):
    length = len(s)
    list(s)
    if s.count('(') != s.count(')'):
        return False
    for j in range(math.ceil(length/2)):
        for i in range(length-1):
            if s[i:i+2] == '()':
                s = s[:i] + s[i+2:]
    return True if s == '' else False

print(
    solution('()()') == True,
    solution('(())()') == True,
    solution(')()(') == False,
    solution('(()(') == False
)
