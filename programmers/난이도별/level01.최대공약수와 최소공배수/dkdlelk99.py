def solution(n, m):
    a, b = max(n,m), min(n,m)
    for i in range(1, b+1):
        if n%i == 0 and m%i == 0:
            a1 = i
    return [a1,a*b//a1]

print(solution(2,5) == [1,10])
print(solution(3,12) == [3,12])
print(solution(12,15) == [3,60])
