# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# https://github.com/DKU-STUDY/Algorithm/blob/master/codility_training/lessons.lesson09.MaximumSliceProblem.MaxDoubleSliceSum/sjjyy.java 참고

def solution(A):
    # write your code in Python 3.6
    pass
    size = len(A)
    L = [0] * size
    R = [0] * size
    mx = 0

    for i in range(1, size):
        L[i] = max(0, L[i-1]+A[i])

    for i in range(size-2, -1, -1):
        R[i] = max(0, R[i+1] + A[i])

    for i in range(1, size-1):
        mx = max(mx, L[i-1] + R[i+1])

    return mx