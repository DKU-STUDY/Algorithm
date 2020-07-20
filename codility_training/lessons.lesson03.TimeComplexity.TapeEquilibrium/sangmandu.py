# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    sum = leftA = sum(A)
    
    min = abs(sum - 2 * A[0])
    for n in range(len(A)-1):
        leftA += A[n]
        min = min([abs(sum - 2 * leftA), min])
            
    return min

print(
    solution([3,1,2,4,3]) == 1,
    # solution(A) == result,
)
