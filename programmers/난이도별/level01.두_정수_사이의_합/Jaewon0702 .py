def solution(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


print(solution(3, 5) == 12)
print(solution(3, 3) == 3)
print(solution(5, 3) == 12)
