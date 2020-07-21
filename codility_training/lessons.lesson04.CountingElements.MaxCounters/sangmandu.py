# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    pass
    arr = [0] * N
    tog = 0
    mx = 0
    for i in A:
        if(i == N+1):
            if(tog == 0):
                tog = 1
                arr = [mx] * N
            continue
        arr[i-1] += 1
        mx = max(arr[i-1], mx)
        tog = 0
    return arr

print(
    solution(1,[1,1,1,2]) == [3]
    # solution(X,A) == result,
)

'''
print(
    solution(5,[3,4,4,6,1,4,4]) == [3,2,2,4,2]
    # solution(X,A) == result,
)
'''
