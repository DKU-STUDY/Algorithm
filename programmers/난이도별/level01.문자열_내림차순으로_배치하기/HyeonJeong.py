# 정렬이 소문자 -> 대문자 됨.
def solution(s):
    return "".join(sorted(s, reverse = True))

print(solution("Zbcdefg") == "gfedcbZ")