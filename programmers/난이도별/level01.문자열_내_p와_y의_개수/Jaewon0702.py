def solution(s):
    return s.lower().count("p") == s.lower().count("y")


# 100점


print(solution("pPoooyY") == True)
print(solution("Pyy") == False)
