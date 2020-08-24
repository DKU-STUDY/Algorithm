def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        print(sum(d[:i+1]))
        if budget < sum(d[:i+1]):
            return i
    return len(d)


print(
    solution([2, 2, 3, 3], 10),
    # solution([1, 3, 2, 5, 4], 9)
)
