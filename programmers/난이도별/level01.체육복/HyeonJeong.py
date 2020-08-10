def solution(n, lost, reserve):
    rest = list(lost)
    for p in lost:
        if p in reserve:
            reserve.remove(p)
            rest.remove(p)
        elif (p - 1) in reserve:
                reserve.remove(p - 1)
                rest.remove(p)
        elif (p + 1) in reserve:
                reserve.remove(p + 1)
                rest.remove(p)
    return n - len(rest)

print(
    solution(5,[2,4],[1,3,5]) == 5,
    solution(5,[2,4],[3]) == 4,
    solution(3,[3],[1]) == 2
     )