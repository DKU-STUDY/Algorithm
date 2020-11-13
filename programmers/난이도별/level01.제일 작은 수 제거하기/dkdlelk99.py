def solution(arr):
    if len(arr) == 1:
        return [-1]
    arr.remove(min(arr))
    return arr

print(solution([10]) == [-1])
print(solution([10,4,5,2,1]) ==[10, 4, 5, 2])
