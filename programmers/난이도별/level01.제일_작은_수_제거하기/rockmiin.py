def solution(arr):
    tmp=sorted(arr)[0]
    if len(arr)>1:
        arr.remove(tmp)
        return arr
    return [-1]

print(
    solution([4, 1, 2, 3])==[4, 2, 3]
)
