from math import *


def solution(n):
    return -1 if sqrt(n) % 1 else int(pow((sqrt(n) + 1), 2))


print(solution(121) == 144)
print(solution(3) == -1)
