def solution1(n):
    return list(map(int, reversed(str(n))))


def solution2(n):
    return [int(i) for i in reversed(str(n))]


def solution3(n):
    return [int(i) for i in str(n)][::-1]


print(solution1(12345) == [5, 4, 3, 2, 1])
print(solution2(12345) == [5, 4, 3, 2, 1])
print(solution3(12345) == [5, 4, 3, 2, 1])
