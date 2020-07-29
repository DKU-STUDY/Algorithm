# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# 굉장히 어려워서 오래걸렸다. 획기적인 발상으로 한번에 풀린 문제

def solution(A):
    # write your code in Python 3.6
    pass
    B = sorted([ i - v for i, v in enumerate(A)  ])
    C = sorted([ i + v for i, v in enumerate(A)  ])

    num = len(A)
    case = num * (num - 1) // 2
    cnt = 0
    j = 0
    for i in range(len(A)):
        while (C[j] < B[i]):
            cnt += num - i
            j += 1

    return case - cnt if case - cnt <= 10000000 else -1
