# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    B = {}
    D = set(A)

    for i in D:
        B[i] = 0

    for i in A:
        B[i] += 1

    equi = 0
    for k, v in B.items():
        if (v > len(A) // 2):
            equi = k

    cnt = ret = 0
    num = B.get(equi)
    size = len(A)
    for i, v in enumerate(A):
        if v == equi:
            cnt += 1
        if (i + 1) / 2 < cnt and (size - i - 1) / 2 < num - cnt:
            ret += 1

    return ret

print(
    solution(4, 3, 4, 4, 4, 2 == 2)
)