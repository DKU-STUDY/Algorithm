def solution(x):
    total = 0
    num = x
    for i in str(x):
        if num > 0:
            total += num % 10
            num = num // 10
    return x % total == 0