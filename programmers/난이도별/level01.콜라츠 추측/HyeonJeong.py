def solution(num):
    tries = 0
    while num != 1:
        num = num // 2 if num % 2 == 0 else num * 3 + 1
        tries += 1
        if tries == 500:
            return -1
    return tries