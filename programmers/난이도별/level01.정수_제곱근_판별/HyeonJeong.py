def solution(n):
    for i in range(1, n + 1):
        if n ** 0.5 == i:
            return (i + 1) ** 2
        elif i == n:
            return -1

print(solution(121) == 144)