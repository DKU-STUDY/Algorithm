def solution(A, K):
    length_of_A = len(A)
    if length_of_A == 0:
        return A
    cutter = K % length_of_A
    left_list = A[:-cutter]
    rigth_list = A[-cutter:]
    return rigth_list + left_list

A = [1,2,3,4,5,6]
for i in range(2*len(A)):
    K = i
    print(f'K = {i}')
    print(solution(A,i))