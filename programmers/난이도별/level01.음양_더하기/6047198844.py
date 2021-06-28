def solution(absolutes, signs):
    return sum([absolute if sign else -absolute for absolute, sign in zip(absolutes, signs)])