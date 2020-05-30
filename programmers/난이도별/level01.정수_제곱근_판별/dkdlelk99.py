def solution(n):
    for i in range(n+1):
        if i*i == n:
            return (i+1)**2
    return -1

print(solution(121) == 144)
print(solution(3) == -1)
