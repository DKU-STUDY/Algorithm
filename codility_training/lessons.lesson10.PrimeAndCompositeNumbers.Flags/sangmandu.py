def solution(A):
    # write your code in Python 3.6
    pass
    B = []
    for i in range(1, len(A) - 1):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            B.append(i)

    size = len(B)
    if size == 0:
        return 0

    C = [ B[i] - B[i - 1] for i in range(1, size) ]

    maxFlags = 1
    for i in range(2, size + 1):
        flags = 1
        dist = 0
        for j in C:
            dist += j
            if flags == i:
                break
            if dist < i:
                continue
            flags += 1
            dist = 0
        maxFlags = max(maxFlags, flags)
        if flags != i and maxFlags != flags:
            break
    return maxFlags

print(
    solution([1,5,3,4,3,4,1,2,3,4,6,2] == 3)
)
