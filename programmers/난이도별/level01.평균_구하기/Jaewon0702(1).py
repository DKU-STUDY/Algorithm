import numpy


def solution(arr):
    return numpy.mean(arr)


print(solution([1, 2, 3, 4]) == 2.5)
print(solution([5, 5]) == 5)
