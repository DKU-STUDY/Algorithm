def solution(s):
    s = s.lower()
    print(s)
    return s.count('p') == s.count('y')

print(solution("oooo") == True)
print(solution('pPooYy') == True)
print(solution("pPPYy") == False)
