#1
'''def solution(s):
    if "+-" not in s:
        return int(s)
    return int(+s[1:]) if s[0] == "+" else int(-s[1:])'''

#2 s가 정수일 때 가능함
def solution(s):
    return int(s)

print(solution("-1234") == -1234)