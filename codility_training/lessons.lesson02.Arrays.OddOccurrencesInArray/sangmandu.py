
def solution(A):
	sA = sorted(A)
	if len(sA) == 0:
		return sA[2*i]
	for i in range(len(sA)//2):
		if sA[2*i] != sA[2*i+1]:
			return sA[2*i]
	
