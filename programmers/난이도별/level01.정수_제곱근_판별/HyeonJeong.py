def solution(n):
    for i in range(1, n + 1):
        if i * i == n:
            return (i + 1) * (i + 1)
        elif i == n:
            return -1

print(solution(121) == 144)