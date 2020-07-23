# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    pass
    ret = []
    for i in range(len(P)):
        temp = S[P[i]:Q[i] + 1]
        if temp.find("A") != -1:
            ret.append(1)
        elif temp.find("C") != -1:
            ret.append(2)
        elif temp.find("G") != -1:
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
