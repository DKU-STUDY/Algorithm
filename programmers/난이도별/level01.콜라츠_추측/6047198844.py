def solution(num):
    for cnt in range(501):
        if num == 1:
            return cnt
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
    return -1