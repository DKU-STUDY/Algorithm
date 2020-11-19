def solution(s):
    return "".join(sorted(list(s), reverse=True))


# 100점


print(solution("Zbcdefg") == "gfedcbZ")
