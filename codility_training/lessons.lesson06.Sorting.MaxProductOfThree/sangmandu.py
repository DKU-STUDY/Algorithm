# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    sA = sorted(A)
    size = len(sA)
    mx1 = sA[size-1] * sA[size-2] * sA[size-3]
    mx2 = sA[size-1] * sA[0] * sA[1]
    return mx1 if mx1 > mx2 else mx2
    
    '''
    + + + 큰 수들로 곱
    + + - 작은수들로 곱 // not applied
    + - - 큰 수들로 곱
    - - - 작은수들로 곱 // not applied
    '''

print(
	solution([-3, 1, 2, -2, 5, 6]) == 60
	)