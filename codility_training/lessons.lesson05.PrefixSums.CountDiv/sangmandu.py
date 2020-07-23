# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    pass
    return B // K - A // K + (1 if A % K == 0 else 0)


print(
    solution(6, 12, 2) == 4
)