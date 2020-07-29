# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    pass
    S = []
    cnt = 0

    for i, v in enumerate(A):
        if B[i] == 1:
            S.append(v)
            continue;
        while len(S) != 0:
            fish = S.pop()
            if fish > v:
                S.append(fish)
                break
        if (len(S) == 0):
            cnt += 1

    return cnt + len(S)

pritn(
    solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) == 2
)
