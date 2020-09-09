# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    pass

    i = 1
    while i * i <= N: i += 1
    i -= 1
    
    cnt = 0
    for j in range(1, i + 1):
        cnt += 1 if N % j == 0 else 0
        j += 1

    return (cnt * 2 if i * i != N else cnt * 2 - 1)

print(
    solutiion(24) == 8
)
