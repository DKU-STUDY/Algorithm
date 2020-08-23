def solution(s):
    return s.isdigit() if len(s) in [4, 6] else False


# 100점


print(solution("a234"))
print(solution("1234"))
