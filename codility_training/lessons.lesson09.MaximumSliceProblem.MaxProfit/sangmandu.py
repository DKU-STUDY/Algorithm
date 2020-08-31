# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass

    B = []
    if len(A) == 0:
        return 0
    mn = A[0]

    for i in A[1:]:
        mn = min(mn, i)
        B.append(i - mn)

    B.sort()
    return B[-1]

print(
    solutiion(23171, 21011, 21123, 21366, 21013, 21367) == 356
)