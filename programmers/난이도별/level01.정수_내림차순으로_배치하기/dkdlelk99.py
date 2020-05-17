def solution(n):
    s = str(n)
    a = list(s)
    a.sort()
    a.reverse()
    answer = ''.join(a)
    return int(answer)

print(solution(118372) == 873211)
print(solution(12421356) == 65432211)
