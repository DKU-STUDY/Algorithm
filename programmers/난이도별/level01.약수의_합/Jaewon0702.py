def solution(n):
    return sum([n] + [i for i in range(1, n // 2 + 1) if n % i == 0])


print(solution(12) == 28)
print(solution(5) == 6)
