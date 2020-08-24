def solution(n, lost, reserve):
    n_lost = set(lost) - set(reserve)
    n_reserve = set(reserve) - set(lost)
    for p in n_reserve:
        if (p - 1) in n_lost:
            n_lost.remove(p - 1)
        elif (p + 1) in n_lost:
            n_lost.remove(p + 1)
    return n - len(n_lost)

print(
    solution(5,[2,4],[1,3,5]) == 5,
    solution(5,[2,4],[3]) == 4,
    solution(3,[3],[1]) == 2
     )