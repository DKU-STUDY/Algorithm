# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    pass
    ret = []
    for i in range(len(P)):
        if S.find("A",P[i],Q[i]+1) != -1:
            ret.append(1)
        elif S.find("C",P[i],Q[i]+1) != -1:
            ret.append(2)
        elif S.find("G",P[i],Q[i]+1) != -1:
            ret.append(3)
        else:
            ret.append(4)
    return ret

print(
    solution('A', [0], [0]) == [1]
)

print(
    solution('CAGCCTA', [2, 5, 0], [4, 5, 6]) == [2, 4, 1]
)
