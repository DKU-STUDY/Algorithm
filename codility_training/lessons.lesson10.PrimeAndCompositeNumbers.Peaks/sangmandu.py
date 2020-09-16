# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    B = [i for i in range(1, len(A) - 1) if max(A[i - 1], A[i + 1]) < A[i]]

    sizeB = len(B)
    if len(B) == 0:
        return 0

    sizeA = len(A)
    sqrt = int(sizeA ** (1 / 2))
    div = [sizeA // i for i in range(1, sqrt + 1) if sizeA % i == 0 and i <= sizeB]

    temp = []
    for i in div[::-1]:
        if i > sizeB:
            break
        temp.append(sizeA // i)
    div += temp

    maxBlank = 0
    for i in div:
        blank = [B[j] // i for j in range(sizeB)]
        if len(set(blank)) == sizeA // i:
            maxBlank = max(maxBlank, sizeA // i)
    return maxBlank

print(
    solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]) == 3
)
