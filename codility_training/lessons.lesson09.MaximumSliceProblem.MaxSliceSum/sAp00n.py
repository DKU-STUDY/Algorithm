def solution(A):
    maximum = A[0]
    temp = 0
    for i in A:
        temp = temp+i
        temp = max(temp , i)
        maximum = max(temp, maximum)
        #print(f'temp = {temp}       max = {maximum}')
    return maximum