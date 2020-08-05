# you can write to stdout for debugging purposes, e.g..
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    pass
    cnt = 0
    for i in S:
        cnt += 1 if i == "(" else -1

        if (cnt < 0):
            return 0
    return 1 if cnt == 0 else 0

pritn(
    solution("(()(())())") == 1
)
