from datetime import *


def solution(a, b):
    weeks = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return weeks[datetime(2016, a, b).weekday()]


# 100점


print(solution(5, 24) == "TUE")
