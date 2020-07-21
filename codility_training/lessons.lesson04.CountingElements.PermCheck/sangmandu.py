# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    A.sort()
    for i in range(len(A)):
        if i+1 != A[i]:
            return 0
    return 1
    
print(
    solution([4, 1, 3, 2]) == 1,
    solution([4, 1, 3]) == 0
    )