def solution(A):
    start_ind, end_ind = find_max_slice(A)
    max_slice = A[start_ind:end_ind]
    max_slice.remove(min(max_slice))

    return sum(max_slice)


def find_max_slice(A):
    A = A[1:-2]
    maximum = A[0]
    temp = 0
    start_ind = 0
    end_ind = 0
    for i in A:
        if i > temp + i:
            start_ind = A.index(i)
        temp = max(temp + i, i)
        if temp > maximum:
            end_ind = A.index(i)
        maximum = max(temp, maximum)
        # print(f'temp = {temp}       max = {maximum}\n A[{start_ind}:{end_ind}]')
    return start_ind, end_ind
