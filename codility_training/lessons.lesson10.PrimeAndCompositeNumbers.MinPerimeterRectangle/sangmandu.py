# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    pass

    M = N ** (1 / 2)
    M = int(M)
    for i in range(M, 0, -1):
        if N % i == 0:
            return int(N / i + i) * 2
print(
    solution(30) == 22
)