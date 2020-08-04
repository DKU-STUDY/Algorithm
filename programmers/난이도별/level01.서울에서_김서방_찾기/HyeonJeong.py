def solution(seoul):
    for m, n in enumerate(seoul):
        if "Kim" == n:
            return ("김서방은 %d에 있다" %m)
            # return "김서방은 {}에 있다".format(m)

print(solution(["Jane","Kim"]) == "김서방은 1에 있다")