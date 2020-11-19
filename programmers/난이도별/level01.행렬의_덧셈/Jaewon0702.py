def solution1(arr1, arr2):
    return [
        [arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))
    ]


import numpy as np


def solution2(arr1, arr2):
    return (np.array(arr1) + np.array(arr2)).tolist()


print(solution1([[1, 2], [2, 3]], [[3, 4], [5, 6]]) == [[4, 6], [7, 9]])
print(solution2([[1, 2], [2, 3]], [[3, 4], [5, 6]]) == [[4, 6], [7, 9]])
