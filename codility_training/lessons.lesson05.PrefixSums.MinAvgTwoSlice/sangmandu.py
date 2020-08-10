# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    mn2 = sum(A[0:2]) / 2
    idx2 = idx3 = 0
    for i in range(1, len(A)-1):
        if mn2 > sum(A[i:i+2]) / 2:
            mn2 = sum(A[i:i+2]) / 2
            idx2 = i
    
    if(len(A) >= 3):
	    mn3 = sum(A[0:3]) / 3
	    for i in range(1, len(A)-2):
	    	if mn3 > sum(A[i:i+3]) / 3:
	            mn3 = sum(A[i:i+3]) / 3
	            idx3 = i
	    return idx2 if sum(A[idx2:idx2+2])/2 <= sum(A[idx3:idx3+3])/3 else idx3
	    
    return idx2

print(
    solution([-1,-1,0,-1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,0,0,0])
)