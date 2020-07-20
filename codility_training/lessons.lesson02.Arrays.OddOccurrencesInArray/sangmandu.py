
def solution(A):
	sA = sorted(A)
        size = len(sA)
	if size == 0:
		return sA[2*i]
	for i in range(size // 2):
		if sA[2 * i] != sA[2 * i + 1]:
			return sA[2 * i]

	
