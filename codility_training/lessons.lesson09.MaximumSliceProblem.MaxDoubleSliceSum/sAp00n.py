# test case [5, 17, 0, 3], [0, 10, -5, -2, 0], [5, 5, 5] and all negative

def solution(A):
    if len(A) <= 3:
        return 0
    else:
        B = A[1:-1]
        print(f'B = {B}')
        start_ind, end_ind = find_max_slice(B)

        resulte = B[start_ind:end_ind]
        if end_ind == None:
            print(f'B[{start_ind}:{end_ind}] =  [{A[start_ind]} {resulte} {A[-1]}]')
        else:
            print(f'B[{start_ind}:{end_ind}] =  [{A[start_ind]} {resulte} {A[end_ind + 1]}]')
        if len(resulte) == 1:
            if resulte[0] > 0:
                return resulte[0]
            else:
                return 0
        else:
            resulte.remove(min(resulte))
            return sum(resulte)


def find_max_slice(A):
    maximum = A[0]
    temp = A[0]
    start_ind = 0
    end_ind = 1
    for i in range(len(A)):
        if A[i] >= temp + A[i]:
            start_ind = i
            end_ind = i + 1
        temp = max(temp + A[i], A[i])
        if temp >= maximum:
            end_ind = i + 1
        maximum = max(temp, maximum)
        """print(f'temp = {temp}       max = {maximum}')
        print(f'A[{start_ind}:{end_ind}] ={A[start_ind:end_ind]}')"""
    if end_ind == len(A):
        end_ind = None
    return start_ind, end_ind
