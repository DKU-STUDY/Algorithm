def solution(num):
    n = 0
    while num > 1:
        num = num * 3 + 1 if num % 2 else num / 2
        n += 1
        if n == 500:
            return -1
    return n


print(solution(6) == 8)
print(solution(16) == 4)
print(solution(626331) == -1)
