def solution(arr, divisor):
    return sorted([v for v in arr if v % divisor == 0]) or [-1]


# 100점


print(solution([5, 9, 7, 10], 5) == [5, 10])
print(solution([2, 36, 1, 3], 1) == [1, 2, 3, 36])
print(solution([3, 2, 6], 10) == [-1])
