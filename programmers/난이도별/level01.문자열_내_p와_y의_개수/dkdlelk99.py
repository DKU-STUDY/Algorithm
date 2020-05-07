def solution(s):
    s = s.lower()
    print(s)
    p, y = s.count('p'), s.count('y')
    if p == y:
        return True
    return s.count('p') == s.count('y')

print(solution("oooo") == True)
print(solution('pPooYy') == True)
print(solution("pPPYy") == False)
