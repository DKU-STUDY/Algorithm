def solution(n):
    n = str(n)
    s = 0
    for i in n:
        s += int(i)
    return s
    
print(solution(21) == 3)
print(solution(123) == 6)
