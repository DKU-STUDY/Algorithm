def solution(s):
    return s.isdigit() and len(s) in [4, 6]


# 100점


print(solution("a234"))
print(solution("1234"))
