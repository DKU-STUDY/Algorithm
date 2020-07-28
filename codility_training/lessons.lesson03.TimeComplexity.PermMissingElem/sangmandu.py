# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    sum = sum(A)
    n = len(A)
    return (n + 2) * ((n + 1) // 2) + (0 if n % 2 == 1 else  (n + 2) // 2) - sum

print(
    solution([2,3,1,5]) == 4,
    # solution(A) == result,
)

