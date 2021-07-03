def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]