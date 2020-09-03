# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    size = len(A)
    L = [0] * size
    mx = 0

    if sorted(A)[-1] < 0:
        return sorted(A)[-1]

    for i in A:
        mx = max(0, mx + i)
        L.append(mx)

    return sorted(L)[-1]

print(
    solutiion(3, 2, -6, 4, 0) == 5
)