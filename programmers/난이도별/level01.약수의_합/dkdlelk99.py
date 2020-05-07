def solution(n):
    d = []
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            d.append(i)
    print(d)
    for i in d:
        answer += i
    return answer

print(solution(12) == 28)
print(solution(6) == 12)
