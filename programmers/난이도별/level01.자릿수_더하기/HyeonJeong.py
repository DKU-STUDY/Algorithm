def solution(n):
    answer = 0
    for i in range(1, 10):
        answer += n % 10
        n = n // 10
    return answer

print(
    solution(123) == 6,
    solution(987) == 24
)