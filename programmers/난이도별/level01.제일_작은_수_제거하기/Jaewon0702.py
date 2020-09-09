def solution(arr):
    arr.remove(min(arr))
    return arr if len(arr) else [-1]


print(solution([4, 3, 2, 1]) == [4, 3, 2])
print(solution([10]) == [-1])
