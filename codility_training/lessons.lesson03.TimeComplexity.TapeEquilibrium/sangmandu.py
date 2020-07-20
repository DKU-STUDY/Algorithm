# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    sum = leftA = sum(A)
    
    min = abs(sum - 2 * A[0])
    for n in range(len(A)-1):
        leftA += A[n]
        min = abs(sum - 2 * leftA) if abs(sum - 2 * leftA) < min else min
            
    return min

'''
A[0] = 3
A[1] = 1
A[2] = 2
A[3] = 4
A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
'''
