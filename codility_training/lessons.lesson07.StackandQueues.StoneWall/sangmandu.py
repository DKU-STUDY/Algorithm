# you can write to stdout for debugging purposes, e.g..
# print("this is a debug message")
# 좀 어렵다 문제가.. 전혀 not painless... painful..
def solution(H):
    # write your code in Python 3.6
    pass
    S  = []
    cnt = 0
    for x in H:
        while len(S) > 0 and S[len(S)-1] > x:
            S.pop()
        if len(S) == 0 or S[len(S)-1] < x:
            S.append(x)
            cnt += 1
    return cnt

pritn(
    solution([8,8,5,7,9,8,7,4,8]) == 7
)
