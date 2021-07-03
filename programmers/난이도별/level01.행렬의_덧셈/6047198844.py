def solution(arr1, arr2):
    return [[a+b
             for a, b in zip(a_1, a_2)]
             for a_1, a_2 in zip(arr1, arr2)]
