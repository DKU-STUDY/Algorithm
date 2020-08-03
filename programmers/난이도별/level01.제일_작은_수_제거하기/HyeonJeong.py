def solution(arr):
    if len(arr) == 1:
        return [-1]

    temp = min(arr)
    '''
    min() 없이 풀면
    temp = arr[0]
    for x in range(len(arr)):
        if arr[x] < temp:
            temp = arr[x]
    '''
    for x in arr:
        if x == temp:
            arr.remove(x)
    return arr