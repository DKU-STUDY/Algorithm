def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        if sign:
            answer += absolute
        else:
            answer -= absolute
    return answer