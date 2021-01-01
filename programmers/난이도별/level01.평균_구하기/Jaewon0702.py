import numpy


def solution1(arr):
    return numpy.mean(arr)


def solution2(arr):
    return sum(arr) / len(arr)


print(solution1([1, 2, 3, 4]))
print(solution1([5, 5]))

print(solution2([1, 2, 3, 4]) == 2.5)
print(solution2([5, 5]) == 5)
