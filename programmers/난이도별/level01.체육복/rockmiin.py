def solution(n, lost, reserve):
    dup = []
    for i in reserve:
        if i in lost:
            dup.append(i)
    for i in dup:
        reserve.remove(i)
        lost.remove(i)
    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)
    return n - len(lost)

print(
    solution(5, [2, 4], [1, 3, 5]),
    solution(5, [2, 4], [1, 3, 5]) == 5,
    solution(5, [2, 4], [3]),
    solution(5, [2, 4], [3]) == 4,
)
