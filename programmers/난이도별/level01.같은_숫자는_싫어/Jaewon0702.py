def solution(arr):
    removed = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            removed.append(arr[i])
    return removed


# 100점


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
