def solution(s):
    return ''.join(sorted(list(s), reverse=True))

print(solution("Zbcdefg") == "gfedcbZ")
print(solution("bdcaET") == "dcbaTE")
