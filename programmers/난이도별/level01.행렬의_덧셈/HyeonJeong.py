def solution(arr1, arr2):
    answer = arr1
    for i, x in enumerate(arr2):
        for j, y in enumerate(x):
            answer[i][j] += y
    return answer

print(
    solution([[1,2],[2,3]], [[3,4],[5,6]]) == [[4,6],[7,9]],
    solution([[1],[2]], [[3],[4]]) == [[4],[6]]
)
