def solution(s):
    a = []
    for i in s:
        a.append(i)
    a.sort()
    a.reverse()
    answer = ''.join(a)
    return answer

print(solution("Zbcdefg") == "gfedcbZ")
print(solution("bdcaET") == "dcbaTE")
