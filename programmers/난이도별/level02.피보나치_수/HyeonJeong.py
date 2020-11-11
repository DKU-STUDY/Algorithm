def solution(n):
    fibo = [0, 1]
    for i in range(2, n + 1):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    return fibo[-1] % 1234567

print(
    solution(3) == 2,
    solution(5) == 5
)
