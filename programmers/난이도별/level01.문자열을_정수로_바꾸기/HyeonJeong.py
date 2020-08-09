def solution(s):
    if "+-" not in s:
        return int(s)
    return int(+s[1:]) if s[0] == "+" else int(-s[1:])

print(solution("-1234") == -1234)