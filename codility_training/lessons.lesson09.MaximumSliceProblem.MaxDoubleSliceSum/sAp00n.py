# test case [5, 17, 0, 3], [0, 10, -5, -2, 0], [5, 5, 5] and all negative

def solution(A):
    mid = 1
    total = 0
    max_slice = 0

    for idx, end in enumerate(A[2:-1], start=2):

        if total < 0:
            mid = idx
            total = 0

        elif total == 0 and A[idx - 1] > A[mid]:
            mid = idx - 1
            total = end

        else:
            if A[mid] > end:
                total += A[mid]
                mid = idx
            else:
                total += end

        max_slice = max(max_slice, total)

    return max_slice