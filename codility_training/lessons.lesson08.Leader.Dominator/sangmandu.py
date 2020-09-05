# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    B = {}
    C = set(A)

    for i in C:
        B[i] = 0

    for i in A:
        B[i] += 1

    for k, v in B.items():
        if (v > len(A) // 2):
            return A.index(k)
    return -1

print(
    solution(3,4,3,2,3,-1,3,3 == 0)
)