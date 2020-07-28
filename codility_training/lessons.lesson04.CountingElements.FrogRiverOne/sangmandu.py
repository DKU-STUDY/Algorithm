# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    pass
    sA = set([])
    for idx in range(len(A)):
        sA.add(A[idx])
        if(len(sA) == X):
            return idx
    return -1

print(
    solution(5,[1,3,1,4,2,3,5,4]) == 6,
    # solution(X,A) == result,
)
