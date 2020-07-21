# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    A = sorted(list(set(A)))
    if(A[len(A)-1] <= 0):
        return 1
    while A[0] <= 0:
    	A.pop(0)
    for i in range(len(A)):
    	if i+1 != A[i]:
            return i+1
    return len(A)+1


print(
    solution([-3, -3, -1, -2, -5, -112, 1, 3, 6,-123, -2, 4, 1, 2, -6, -12]) == 5
    # solution(X,A) == result,
)


