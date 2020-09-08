def solution(citations):
    list = []
    cit = sorted(citations, reverse = True)
    for m in range(len(cit)+1):
        max = 0
        for n in cit:
            if n < m:
                break
            max += 1
        if max >= m:
            list += [m]
    list.sort()
    return list[-1]

print(solution([3, 0, 6, 1, 5]) == 3)
